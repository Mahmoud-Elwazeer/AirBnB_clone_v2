#!/usr/bin/env bash
#  sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
ufw allow 'Nginx HTTP'

mkdir -p /data/ /data/web_static/ /data/web_static/releases/
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

data="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$data" > /data/web_static/releases/test/index.html

ln -s /data/web_static/releases/test/ /data/web_static/current

chown ubuntu:ubuntu /data/

conf="server {
        listen 80 default_server;
        server_name mahmoudelwazeer.tech;

        location /hbnb_static/{
                alias /data/web_static/current/;
        }

}"

echo "$conf" > "/etc/nginx/conf.d/hbnb.conf"
