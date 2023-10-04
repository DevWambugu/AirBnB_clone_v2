#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo
'''
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    '''this function generates a .tgz achive for
    webstatic contents'''
    current_time_date = datetime.now()
    timestamp = current_time_date.strftime("%Y%m%d%H%M%S")
    archive_filename = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_filename)

    if not os.path.exists("versions"):
        os.makedirs("versions")
    result = local("tar -cvzf {} web_static".format(archive_path))
    if result.succeeded:
        return archive_path
    else:
        return None
