#!/usr/bin/python3
"""
Creates and distributes an archive to your
web servers, using the function deploy
"""

import os
from fabric.api import *


env.hosts = ['34.229.203.168', '34.207.117.5']


def do_clean(num=0):
    """
    Delete out-of-date archives.
    Args:
        num (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive.
    If number is 2, keeps the most and second-most recent archives,
    etc.
    """
    num = 1 if int(num) == 0 else int(num)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(num)]

    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(num)]
        [run("rm -rf ./{}".format(a)) for a in archives]
