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
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split('/')[-1].split('.')[0]
        sudo("mkdir -p /data/web_static/releases/{}/".format(file))
        sudo("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
             .format(file, file))
        sudo("rm /tmp/{}.tgz".format(file))
        sudo("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(file, file))
        sudo("rm -rf /data/web_static/releases/{}/web_static".format(file))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current"
             .format(file))
        return True
    except Exception:
        return False

def deploy():
    """
    Full deployment of after task
    """
    archive_path = do_pack()
    if archive_path:
        do_deploy(archive_path)
    else:
        return False
