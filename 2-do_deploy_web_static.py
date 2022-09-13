#!/usr/bin/python3
"""
Creates and distributes an archive to your
web servers, using the function deploy
"""

import os
from fabric.api import *
from os.path import isdir
from datetime import datetime

env.hosts = ['34.229.203.168', '34.207.117.5']


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


def do_deploy(archive_path):
    """
    Returns True if all operations have been done correctly,
    otherwise returns False
    """
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        print(a_path)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))

        return True

    return False
