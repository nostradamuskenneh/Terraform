#Bash If Statement Examples ( If then fi, If then else fi, If elif else fi, Nested if )

`In Bash, we have the following conditional statements:`
    - if..then..fi statement (Simple If)
    - if..then..else..fi statement (If-Else)
    - if..elif..else..fi statement (Else If ladder)
    - if..then..else..if..then..fi..fi..(Nested if)


#------------------------Bash If..then..fi statement-----------------------

#!/bin/bash
if [ conditional expression ]
then
  statement1
  statement2
  .
fi

#!/bin/bash
count=100
if [ $count -eq 100 ]
then
  echo "Count is 100"
fi


#!/bin/bash
echo -n "Enter a number: "
read VAR
 
if [[ $VAR -gt 10 ]]
then
  echo "The variable is greater than 10."
fi


#!/bin/bash
read -p "Enter a number: " NUMBER
if [[ $NUMBER -gt 10 ]]
then
  echo "The variable is greater than 10."
fi



#!/bin/bash
echo "checking OS distribution"
OS=$(cat /etc/os-release | grep -w PRETTY_NAME | awk '{print $1}' | awk -F'"' '{print $2}')
echo "you are running on $OS"
echo

if 
[[ $OS != Ubuntu ]]
then 
echo "the OS is NOT ubuntu this script will not be terminated"
exit 1
fi 



#!/bin/bash
echo "cameroon"
echo "gabon"
echo "senegal"
echo "nigeria"
echo "zambia"

read -p "Chose from the list above: " COUNTRY

if 
[[ $COUNTRY == cameroon ]]
then 
    echo "you are from cameroon"
elif [[ $COUNTRY == gabon ]]
then 
    echo "you are from gabon"
elif [[ $COUNTRY == senegal ]]
then 
    echo "you are from senegal"
elif [[ $COUNTRY == nigeria ]]
then 
    echo "you are from nigeria"
elif [[ $COUNTRY == zambia ]]
then 
    echo "you are from zambia"
else
    echo "your citizenship is not amount the list provided above"
fi