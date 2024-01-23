#!/usr/bin/env bash
# 404 redirection with nginx

sudo apt update -y
sudo apt upgrade -y
sudo apt install nginx -y
sudo service nginx start

# Create a custom index page with "Ceci n'est pas une page"
echo "Ceci n'est pas une page" | sudo tee /var/www/html/index.nginx-debian.html

# Add redirection for /redirect_me
new_string='server_name _;\n\n\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
sudo sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-available/default

# Configure custom 404 page
sudo sed -i 's/^\t}$/\t}\n\n\terror_page 404 \/404.html;/' /etc/nginx/sites-available/default

# Create a custom 404 page with "Ceci n'est pas une page"
echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html

sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
