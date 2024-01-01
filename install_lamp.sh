
#!/bin/bash

# Update and Upgrade the Pi, Ensures we're running on the latest software
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Apache2
sudo apt-get install apache2 -y

# Install MySQL
sudo apt-get install mariadb-server -y
# Secure your installation. You'll be prompted to enter some details
sudo mysql_secure_installation

# Install PHP
sudo apt-get install php -y
sudo apt-get install php-mysql -y

# Restart Apache to load the new PHP module
sudo service apache2 restart

echo "LAMP stack installed successfully!"

