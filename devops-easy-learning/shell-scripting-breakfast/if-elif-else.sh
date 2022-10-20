##-----------Bash If..elif..else..fi--------------------
If [ conditional expression1 ]
then
  statement1
  statement2
  .
elif [ conditional expression2 ]
then
  statement3
  statement4
  .
.
.
else
  statement5
fi


#!/bin/bash
count=99
if [ $count -eq 100 ]
then
  echo "Count is 100"
elif [ $count -gt 100 ]
then
  echo "Count is greater than 100"
else
  echo "Count is less than 100"
fi



#!/bin/bash
if [ $UID -ne 0 ]
then
        echo -e "\nPlease, you need root access to run this script.....\n"
        exit 0
fi
echo -e "\nPlease make a choice below:   \n
        *********************************
        *       1==> nproc              *
        *       2==> Memory             *
        *       3==> Os version         *
        *       4==> processes          *
        *       5==> system bits        *
        *       6==> mount points       *
        *       7==> ip address         *
        *       8==> Hostname           *
        *       9==> Kernel version     *
        *       10==> update OS         *
        *********************************\n"

echo -n "Enter your choice (1 - 10):   "
read ans


if  [ ${ans} -eq 1 ] 
then
lscpu

elif  [ ${ans} -eq 2 ]
then
free -h

elif [ ${ans} -eq 3 ]
then
cat /etc/*release

elif [ ${ans} -eq 4 ] 
then
ps -ef

elif [ ${ans} -eq 5 ]
then
getconf LONG_BIT

elif [ ${ans} -eq 6 ]
then
df -h

elif  [ ${ans} -eq 7 ] 
then
ip a

elif  [ ${ans} -eq 8 ]
then
hostname

elif  [ ${ans} -eq 9 ] 
then
uname -r

elif  [ ${ans} -eq 10 ] 
then
yum update -y

else
echo -e "\nPlease enter a valid choice (1- 10) \n"
exit 0
fi