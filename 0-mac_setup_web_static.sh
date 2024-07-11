#!/usr/bin/env bash

# Ensure Nginx is installed
if ! brew list nginx &>/dev/null; then
  echo "Nginx is not installed. Installing Nginx..."
  brew install nginx
fi

# Start Nginx service
brew services start nginx

# Create necessary directories if they don't already exist
sudo mkdir -p /usr/local/var/www/data/web_static/releases/test/
sudo mkdir -p /usr/local/var/www/data/web_static/shared/

# Create a fake HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /usr/local/var/www/data/web_static/releases/test/index.html

# Create a symbolic link, forcefully delete if it already exists
sudo ln -sf /usr/local/var/www/data/web_static/releases/test/ /usr/local/var/www/data/web_static/current

# Give ownership of /usr/local/var/www/data/ folder to the current user and group recursively
sudo chown -R $(whoami):staff /usr/local/var/www/data/

# Update Nginx configuration to serve content
nginx_conf="/usr/local/etc/nginx/nginx.conf"
if ! grep -q "location /hbnb_static/" "$nginx_conf"; then
  sudo sed -i '' '/server_name  localhost;/a \
  location /hbnb_static/ {\
      alias /usr/local/var/www/data/web_static/current/;\
  }\
  ' "$nginx_conf"
fi

# Restart Nginx to apply changes
sudo brew services restart nginx

# Exit successfully
exit 0
