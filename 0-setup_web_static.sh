#!/usr/bin/env bash
#  sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y

sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

data="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$data" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

conf="server {
        listen 80 default_server;
        index index.html index.htm;
        server_name mahmoudelwazeer.tech;
        add_header X-Served-By $HOSTNAME;
        root /data/web_static;

        location /hbnb_static/{
                alias /data/web_static/current/;
        }

}"

echo "$conf" | sudo tee /etc/nginx/conf.d/hbnb.conf
sudo service nginx start
