#!/usr/bin/python3

# Import Fabric API
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers
"""
import os
from datetime import datetime
from fabric.api import local, runs_once


# Define the function 'do_pack'
@runs_once
def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""
    # Create the 'versions' folder if it doesn't exist
    local("mkdir -p versions")

    # Format the current datetime
    now = datetime.now()
    dt_format = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(dt_format)

    # Create the .tgz archive
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    else:
        return archive_path
