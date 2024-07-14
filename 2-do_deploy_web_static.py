#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers
"""
from fabric.api import env, run, put
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']  # Update with your web server IPs
env.user = 'ubuntu'  # Update with your SSH username
env.key_filename = '~/.ssh/<your_private_key>'  # Update with the path to your private SSH key


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>/
        archive_filename = archive_path.split('/')[-1]
        archive_no_ext = archive_filename.split('.')[0]
        releases_path = "/data/web_static/releases/{}/".format(archive_no_ext)
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, releases_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Move contents from extracted folder to releases path
        run("mv {}web_static/* {}".format(releases_path, releases_path))

        # Remove empty folder
        run("rm -rf {}web_static".format(releases_path))

        # Update the symbolic link /data/web_static/current
        current_path = "/data/web_static/current"
        run("rm -rf {}".format(current_path))
        run("ln -s {} {}".format(releases_path, current_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
