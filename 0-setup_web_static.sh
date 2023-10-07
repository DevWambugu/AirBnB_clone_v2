#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo printf "<html>
  <head>
   </head>
    <body>
      Holberton School
    </body>
   </html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -fs /data/web_static/releases/test/* /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
loc_header="location \/hbnb\_static\/ {"
loc_content="alias \/data\/web\_static\/current\/;"
new_location="\n\t$loc_header\n\t\t$loc_content\n\t}\n"
sudo sed -i "37s/$/$new_location/" /etc/nginx/sites-available/default
sudo service nginx restart
