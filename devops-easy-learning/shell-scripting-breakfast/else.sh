##-----------Bash If..then..else..fi statement----------
if [ conditional expression ]
then
  statement1
  statement2
  .
else
  statement3
  statement4
  .
fi


#!/bin/bash
count=100
if [ $count -eq 100 ]
then
  echo "Count is 100"
else
  echo "Count is not 100"
fi

#!/bin/bash
read -p "Enter the first name: " FIRST_NAME 
read -p "Enter the first name: " LAST_NAME 
read -p "Enter number: " NUMBER 
 
if [[ $NUMBER -gt 10 ]]
then
  echo "Hello ${FIRST_NAME} ${LAST_NAME},The number is greater than 10."
else
  echo "Hello ${FIRST_NAME} ${LAST_NAME}, The number is equal or less than 10."
fi