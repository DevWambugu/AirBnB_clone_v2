#!/usr/bin/python3
'''
The Fabric script is based on the file 1-pack_web_static.py.
It distributes an archive to your web servers,
using the function do_deploy
'''
from fabric.api import run
from fabric.api import env
from fabric.api import put
import os

env.hosts = [52.86.88.220, 54.237.54.125]
env.user = 'ubuntu'
env.key_file_name = "~/.ssh/school"


def do_deploy(archive_path):
    '''Distribute an archice to your serveers
    and deploy it
    '''
    if not os.path.exists(archive_path):
        return False

    archive_filename = os.path.basename(archive_path)
    archive_no_ext = os.path.splitext(archive_filename)[0]
    remote_archive_path = "/tmp/{}".format(archive_filename)
    remote_release_dir = "/data/web_static/releases/{}/".format(archive_no_ext)
    '''upload the compressed file to he remote server'''
    put(archive_path, remote_archive_path)

    '''uncompress the file into the destination folder'''
    run("mkdir -p {}".format(remote_release_dir))
    run("tar -xzf {} -C {}".format(remote_archive_path, remote_release_dir))

    '''remove the archive from the webserver temporary files'''
    run("rm {}".format(remote_archive_path))

    '''Delete and create a new symbolic link on the server'''
    run("rm -f /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(remote_release_dir))

    '''return True if successful'''
    return True
