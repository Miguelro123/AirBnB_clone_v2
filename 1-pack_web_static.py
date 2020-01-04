#!/usr/bin/python3
# Fabric script to generate .tgz archive file

from fabric.api import *
from time import strftime


def do_pack():
    """Fabric script to compress files in web_static"""
    ver = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(ver))
 
   except:
       return None
   return ("versions/web_static_{}.tgz".format(ver))
