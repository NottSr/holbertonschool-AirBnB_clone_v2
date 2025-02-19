#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo
"""

from os.path import isdir
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a tgz archive
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        f_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(f_name))
        return f_name
    except Exception:
        return None
