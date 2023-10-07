#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nginx

# check if folder is present if not create it
FOLDER_PATH="/data/"
FOLDER_PATH2="/data/web_static/"
FOLDER_PATH3="/data/web_static/releases/"
FOLDER_PATH4="/data/web_static/shared/"
FOLDER_PATH5="/data/web_static/releases/test/"

for folder in "$FOLDER_PATH" "$FOLDER_PATH2" "$FOLDER_PATH3" "$FOLDER_PATH4" "$FOLDER_PATH5"; do
    if [ ! -d "$folder" ]; then
            sudo mkdir -p "$folder"
    fi
done

# Create a fake HTML file
echo "
    <html>
      <head>
      </head>
      <body>
        Hello World!     
      </body>
    </html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
# Define source and target paths
SOURCE="/data/web_static/releases/test/"
TARGET="/data/web_static/current"
# Check if the symbolic link already exists and delete it if so
if [ -L "$TARGET" ]; then
    sudo rm -rf "$TARGET"
fi

# create target if it does not already exist
sudo mkdir -p "$TARGET"

# Create the symbolic link
sudo rm -rf "$TARGET/test"
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the folder and its contents to the ubuntu user and group
sudo chown -R ubuntu:ubuntu "$FOLDER_PATH"

# Use sed to insert the location block inside the server block
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart ngix
sudo service nginx restart
