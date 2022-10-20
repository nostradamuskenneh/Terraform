#! /bin/bash

sudo yum update -y
sudo yum install -y wget
sudo yum install -y unzip
sudo yum install -y httpd
sudo systemctl start httpd  
sudo systemctl enable httpd
echo "<h1> At $(hostname -f) Webserver EC2 Instance </h1>" > /var/www/html/index.html