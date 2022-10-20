##-----------Bash If..then..else..if..then..fi..fi..---------

if [ conditional expression1 ]
then
  statement1
  statement2
  .
else
  if [ conditional expression2 ]
  then
    statement3
    .
  fi
fi


#!/bin/bash
count=99
if [ $count -eq 100 ]
then
  echo "Count is 100"
else
  if [ $count -gt 100 ]
  then
    echo "Count is greater than 100"
  else
    echo "Count is less than 100"
  fi
fi


#!/bin/bash
 
echo -n "Enter the first number: "
read VAR1
echo -n "Enter the second number: "
read VAR2
echo -n "Enter the third number: "
read VAR3
 
if [[ $VAR1 -ge $VAR2 ]]  
then
  if [[ $VAR1 -ge $VAR3 ]]
  then
    echo "$VAR1 is the largest number."
  else
    echo "$VAR3 is the largest number."
  fi
else
  if [[ $VAR2 -ge $VAR3 ]]
  then
    echo "$VAR2 is the largest number."
  else
    echo "$VAR3 is the largest number."
  fi
fi


#!/bin/bash

read -p "Enter the first number: " NUMBER1
read -p "Enter the second number: " NUMBER2
read -p "Enter the thirst number: " NUMBER3

if [[ $NUMBER1 -eq $NUMBER2 ]]
then 
  if [[ $NUMBER1 -eq $NUMBER3 ]]
  then
    echo "$NUMBER1, $NUMBER2, $NUMBER3 are equal"
  fi
fi

if [[ $NUMBER1 -eq $NUMBER2 ]]
then 
  if [[ $NUMBER1 -gt $NUMBER3 ]]
  then
    echo "$NUMBER1, $NUMBER2, $NUMBER3 not equal"
  fi
fi

if [[ $NUMBER1 -eq $NUMBER2 ]] && [[ $NUMBER1 -eq $NUMBER3 ]]
then
  echo "$NUMBER1, $NUMBER2, $NUMBER3 are equal"
elif [[ $NUMBER1 -eq $NUMBER2 ]] || [[ $NUMBER1 -gt $NUMBER3 ]]
then
  echo "$NUMBER1, $NUMBER2, $NUMBER3 are not equal"
else
  echo "hummmm"
fi