# Import Fabric API
from fabric.api import local
from datetime import datetime
import os

# Define the function 'do_pack'
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
