#!/usr/bin/python3
'''
The Fabric script is based on the file 1-pack_web_static.py.
It distributes an archive to your web servers,
using the function do_deploy
'''
from fabric.api import run
from fabric.api import env
from fabric.api import put
from fabric.api import sudo
import os

env.hosts = ['52.86.88.220', '100.25.48.51']
env.user = 'ubuntu'
env.key_file_name = "~/.ssh/school"


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


def do_deploy(archive_path):
    '''Distribute an archice to your serveers
    and deploy it
    '''
    if not os.path.exists(archive_path):
        return False

    archive_filename = os.path.basename(archive_path)
    archive_no_ext = os.path.splitext(archive_filename)[0]
    remote_archive_path = "/tmp/{}".format(archive_filename)
    remote_release_dir = "/data/web_static/releases/{}".format(archive_no_ext)
    '''upload the compressed file to he remote server'''
    put(archive_path, remote_archive_path)

    '''uncompress the file into the destination folder'''
    run("mkdir -p {}".format(remote_release_dir))
    run("tar -xzf {} -C {}".format(remote_archive_path, remote_release_dir))

    '''remove the archive from the webserver temporary files'''
    run("rm {}".format(remote_archive_path))

    '''Delete and create a new symbolic link on the server'''
    run("rm -rf /data/web_static/current")
    run("ln -s -f {}/* /data/web_static/current".format(remote_release_dir))

    '''return True if successful'''
    return True

def deploy():
    '''Create and distribute an archive to my webservers'''
    func = do_pack()
    if func is None:
        return False
    return do_deploy(func)
