##-----------Case Statement DAY 01---------

# Syntax of bash case statement.

case EXPRESSION in
 
  PATTERN_1)
    STATEMENTS
    ;;
 
  PATTERN_2)
    STATEMENTS
    ;;
 
  PATTERN_N)
    STATEMENTS
    ;;
 
  *)
    STATEMENTS
    ;;
esac


#!/bin/bash
ENV=$1

case $ENV in
 
  prod | production | Prd | PRD | Prod | Production | PRODUCTION |PROD)
    echo "Deployment to production envirnoment"
    ;;
 
  dev | development| Dev | DEV | DEVELOPMENT)
    echo "Deployment to development envirnoment"
    ;;

  qa | Qa | QA)
    echo "Deployment to QA envirnoment"
    ;;
 
  *)
    echo "Unknown envirnoment"
    ;;
esac




#!/bin/bash
 
echo "Enter the name of a country: "
read COUNTRY
 
echo "The official language of $COUNTRY is "
 
case $COUNTRY in
 
  Lithuania)
    echo "Lithuanian"
    ;;
 
  Romania | Moldova)
    echo "Romanian"
    ;;

  USA | US | us | usa | "United States" | "united states")
    echo "English"
    ;;

  Cameroon | cameroon |camer |kamer | CAMEROON)
    echo "English and Fresh"
    ;;
 
  Italy | "San Marino" | Switzerland | "Vatican City")
    echo "Italian"
    ;;
 
  *)
    echo "unknown"
    ;;
esac



echo "#########################CASE STATEMENT############## CAN ONLY RUN ON UBUNTU###############"
echo  "wget"
echo  "curl"
echo  "vim"
echo  "unzip" 
echo  "tree"
echo  "git"
echo  "default-jre" 
echo  "default-jdk"
echo  "firewalld"
echo  " python3-pip" 
echo  " ansible"
echo  " nodejs" 
echo  " make"
echo  " build-essential" 
echo  " npm"
echo  " ufw"
echo  " apt-utils"

read -p "enter a package from the list above: " PACKAGE

case $PACKAGE in 
    wget | curl | vim | unzip | tree) 
    apt install -y $PACKAGE
    ;;
    git | default-jre)
    apt install -y $PACKAGE
    ;;
    default-jdk |firewalld) 
    apt install -y $PACKAGE
    ;;
    python3-pip | ansible)
    apt install -y $PACKAGE
    ;;
    nodejs |make | build-essential) 
    apt install -y $PACKAGE
    ;;
    npm | ufw | apt-utils)
    apt install -y $PACKAGE
    ;;

    *)
    echo "wronmg selection"
    exit 1
    ;;
esac



#!/bin/bash
apt update -y
A=$(echo $?)

case $A in 

0) 
echo "It looks good"
;; 

*)
  echo "Something went wrong"

  ;;
esac
################################
echo "cameroon"
echo "gabon"
echo "senegal"
echo "nigeria"
echo "zambia"
read -p "Chose from the list above: " COUNTRY
case $COUNTRY in 

cameroon)
 echo "you are from cameroon"
 ;;

 gabon) 

  echo "you are from gabon"
  ;;

senegal)
  echo "you are from senegal"
  ;;
nigeria) 
echo "you are from nigeria"
;;
zambia) 
echo "you are from zambia"
;;
*)
echo "your citizenship is not amount the list provided above"
;;
esac