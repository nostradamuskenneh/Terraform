#! /bin/bash

sudo yum update -y
sudo yum install -y wget
sudo yum install -y unzip
sudo yum install -y httpd
sudo systemctl start httpd  
sudo systemctl enable httpd

cd var/www/html
wget https://linux-devops-course.s3.amazonaws.com/WEB+SIDE+HTML/static-website-example.zip 
unzip static-website-example.zip 
cp -R static-website-example/* . 
rm -rf static-website-example.zip 
rm -rf static-website-example