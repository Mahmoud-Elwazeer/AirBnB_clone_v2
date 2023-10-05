#!/usr/bin/python3
"""import libraries"""
from fabric.api import *
from datetime import datetime

env.hosts = ["54.174.242.67", "54.173.71.78"]
env.user = "ubuntu"


def do_pack():
    """generate tgz"""
    try:
        local("mkdir -p versions")
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        arch_name = f"web_static_{time}.tgz"
        local(f"tar -cvzf versions/{arch_name} web_static")
        return (f"versions/{arch_name}")
    except Exception:
        return None


def do_deploy(archive_path):
    """deploy website"""
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(f"{archive_path}", "/tmp/")
        run(f"makdir -p {path}{no_ext}")
        run(f"tar -xzf /tmp/{file_n} -C {path}{no_ext}/")
        run(f"rm /tmp/{file_n}")
        run(f"mv {path}{no_ext}/web_static/* {path}{no_ext}/")
        run(f"rm -rf {path}{no_ext}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {path}{no_ext}/ /data/web_static/current")
        return True
    except Exception:
        return False
