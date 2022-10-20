#! /bin/bash

# Bamboo server Installation & overview
# https://www.youtube.com/watch?v=f5Z1G0Fw25c
# https://www.hackerxone.com/2022/02/11/steps-to-install-configure-bamboo-on-ubuntu-20-04-lts/

## Installing bamboo
apt-get update -y 
apt-get install -y software-properties-common
apt-get install -y openjdk-8-jdk
apt-get install -y wget
apt-get install -y git

# which  java
# readlink -f /usr/bin/java

JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre"
export JAVA_HOME
PATH=$PATH:$JAVA_HOME
echo $PATH

mkdir -p /home/bamboo-home
cd /opt
wget https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-8.1.2.tar.gz
tar -xvf atlassian-bamboo-8.1.2.tar.gz
mv atlassian-bamboo-8.1.2 bamboo
cd /opt/bamboo/

# Open the following file.
# vim /opt/bamboo/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties
# Un-comment the line.
# #bamboo.home=C:/bamboo/bamboo-home
# Edit the un-commented line.
# bamboo.home=/home/bamboo-home

echo "bamboo.home=/home/bamboo-home" >> /opt/bamboo/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties

# sed -i 'bamboo.home=/home/bamboo-home/d' /opt/bamboo/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties || true
# sed -i 'bamboo.home=/home/bamboo-home' /opt/bamboo/atlassian-bamboo/WEB-INF/classes/bamboo-init.properties

cd /opt/bamboo/bin
./start-bamboo.sh


## MYSQL client command line installation
apt-get install mariadb-client -y

## postgresql client command line installation
apt-get install postgresql-client -y