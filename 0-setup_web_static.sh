#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
if [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install nginx
fi
# check if folder is present if not create it
FOLDER_PATH="/data/"
FOLDER_PATH2="/data/web_static/"
FOLDER_PATH3="/data/web_static/releases/"
FOLDER_PATH4="/data/web_static/shared/"
FOLDER_PATH5="/data/web_static/releases/test/"

if [ -x "$(command -v "$FOLDER_PATH2")" ]; then
    sudo mkdir -p "$FOLDER_PATH2"
fi

if [ -x "$(command -v "$FOLDER_PATH3")" ]; then
	    sudo mkdir -p "$FOLDER_PATH3"
fi

if [ -x "$(command -v "$FOLDER_PATH4")" ]; then
	    sudo mkdir -p "$FOLDER_PATH4"
fi

if [ -x "$(command -v "$FOLDER_PATH5")" ]; then
	    sudo mkdir -p "$FOLDER_PATH5"
fi

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
    sudo rm "$TARGET"
fi
# Create the symbolic link
sudo ln -s "$SOURCE" "$TARGET"

# Give ownership of the folder and its contents to the ubuntu user and group
sudo chown -R ubuntu:ubuntu "$FOLDER_PATH"

# Define the desired URL and path to the HTML file
URL="https://ndonga.tech/hbnb_static"
HTML_FILE="/data/web_static/releases/test/index.html"

# Modify the Nginx configuration using sed
sudo sed -i "/location \/ {/a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

# Test Nginx configuration
sudo nginx -t

# restart ngix
sudo systemctl restart nginx
