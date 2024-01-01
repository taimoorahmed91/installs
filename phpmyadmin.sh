#!/bin/bash

# Update and Upgrade the system
echo "Updating and upgrading the system..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install phpMyAdmin
echo "Installing phpMyAdmin..."
sudo apt-get install phpmyadmin -y

# Configure apache to work with phpMyAdmin
echo "Configuring Apache to work with phpMyAdmin..."
sudo phpenmod mysqli
sudo systemctl restart apache2

echo "phpMyAdmin installation complete. Access it via your web browser."

