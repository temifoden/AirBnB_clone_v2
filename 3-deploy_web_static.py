#!/usr/bin/python3
# Fabfile to create and distribute an archive to web servers.

import os
from datetime import datetime
from fabric.api import env, local, put, run, lcd, cd

env.hosts = ["18.234.80.112", "100.25.133.24"]


def do_pack():
    """
    Create a .tgz archive from the contents of the web_static folder.
    Returns:
        str: The path to the created archive or None if the creation failed.
    """
    local("mkdir -p versions")
    now = datetime.now()
    dt_format = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(dt_format)
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None
    return archive_path


def do_deploy(archive_path):
    """
    Distribute an archive to the web servers.
    Args:
        archive_path (str): The path to the archive to deploy.
    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        filename = archive_path.split("/")[-1]
        foldername = filename.split(".")[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(filename))

        # Uncompress the archive to the folder
        run("mkdir -p /data/web_static/releases/{}/".format(foldername))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, foldername))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # Move the content out of the web_static folder
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(foldername, foldername))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(foldername))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(foldername))

        return True
    except Exception:
        return False


def deploy():
    """
    Create and distribute an archive to the web servers.
    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
