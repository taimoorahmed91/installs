#!/bin/bash

# Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Python 3
echo "Installing Python 3..."
sudo apt-get install python3 -y

# Install pip3 for Python 3
echo "Installing pip3..."
sudo apt-get install python3-pip -y

echo "Python 3 and pip3 installation complete."

