##-----------Bash `AND` - `OR` Operators ---------

The logical OR `||`, `-o` and AND `&&`, `-a` operators allow you to use multiple conditions in the if statements.


#!/bin/bash

read -p "Enter the first number: " NUMBER1
read -p "Enter the second number: " NUMBER2
read -p "Enter the thirst number: " NUMBER3

if [[ $NUMBER1 -eq $NUMBER2 ]] && [[ $NUMBER1 -eq $NUMBER3 ]]
then
  echo "$NUMBER1, $NUMBER2, $NUMBER3 are equal"
elif [[ $NUMBER1 -eq $NUMBER2 ]] || [[ $NUMBER1 -gt $NUMBER3 ]]
then
  echo "$NUMBER1, $NUMBER2, $NUMBER3 are not equal"
else
  echo "hummmm"
fi



#!/bin/bash

read -p "Enter the first number: " NUMBER1
read -p "Enter the second number: " NUMBER2
read -p "Enter the thirst number: " NUMBER3

if [ $NUMBER1 -eq $NUMBER2 -a $NUMBER1 -eq $NUMBER3 ]
then
  echo "$NUMBER1, $NUMBER2, $NUMBER3 are equal"
elif [ $NUMBER1 -eq $NUMBER2 -o $NUMBER1 -gt $NUMBER3 ]
then
  echo "$NUMBER1, $NUMBER2, $NUMBER3 are not equal"
else
  echo "hummmm"
fi



#!/bin/bash
 
echo -n "Enter the first number: "
read VAR1
echo -n "Enter the second number: "
read VAR2
echo -n "Enter the third number: "
read VAR3

if [[ $VAR1 -ge $VAR2 ]] && [[ $VAR1 -ge $VAR3 ]]
then
  echo "$VAR1 is the largest number."
elif [[ $VAR2 -ge $VAR1 ]] && [[ $VAR2 -ge $VAR3 ]]
then
  echo "$VAR2 is the largest number."
else
  echo "$VAR3 is the largest number."
fi



echo "#########################IF STATEMENT############## CAN ONLY RUN ON UBUNTU###############"

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
if 
[[ -z $PACKAGE ]]
 then 
 echo "you provided and empty response this script will be terminated"
 exit 1 
 fi


apt update -y 
if 
[[ $PACKAGE == wget ]] ||  \
[[ $PACKAGE == curl ]]  ||  \
[[ $PACKAGE == vim ]]  ||  \
[[ $PACKAGE == unzip ]] ||  \
[[ $PACKAGE == tree ]] ||  \
[[ $PACKAGE == git ]] ||  \
[[ $PACKAGE == default-jre ]] ||  \
[[ $PACKAGE == default-jdk ]] ||   \
[[ $PACKAGE == firewalld ]]  ||  \
[[ $PACKAGE == python3-pip ]] ||   \
[[ $PACKAGE == ansible ]]  ||  \
[[ $PACKAGE == nodejs ]] ||  \
[[ $PACKAGE == make ]]  ||  \
[[ $PACKAGE == build-essential ]]  ||  \
[[ $PACKAGE == npm ]] ||  \
[[ $PACKAGE == ufw ]]  ||  \
[[ $PACKAGE == apt-utils ]]
then 
    echo "installing $PACKAGE"
    apt install -y $PACKAGE
else
    echo "wrong selection, this script will be terminated"
    exit 1
fi