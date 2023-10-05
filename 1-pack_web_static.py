#!/usr/bin/python3
"""import libraries"""
from fabric.api import *
from datetime import datetime


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
