#!/usr/bin/python3
# Fabfile to delete out-of-date archives
import os
from fabric.api import *

env.hosts = ["18.234.80.112", "100.25.133.24"]


def do_clean(number=0):
    """
    Delete out-of-date archives
    args:
    number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent
    archive. If number is 2, keeps the most recent and
    second-most recent archives. etc
    """
    number = 1 if int(number) == 0 else int(number)

    # local cleaning
    archives = sorted(os.listdir("versions"))
    to_delete = archives[:-number] 
    # [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in to_delete]
    
    # remote cleaning
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        to_delete = archives[:-number]  # keep the most recent 'number' archives
        # [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in to_delete]
