#!/bin/bash
echo "The name of the your computer is: $HOSTNAME"
echo "Your home directory is: $PWD"
echo "Your present working directory is: $HOME"
echo "The Shell being used by the user: $SHELL"


#!/bin/bash
# Store linux comment as varible
testing=`date`
UNAME=`uname -a`
echo "The date and time are: $testing"
echo "The output of uname is: ${UNAME}"


#!/bin/bash
# Users defined variable
days1=10
guest1="Katie"
echo "${guest1} checked in ${days1} days ago"
days2=5
guest2="Jessica"
echo "${guest2} checked in ${days2} days ago"


#!/bin/bash
# assigning a variable value to another variable
value1=10
value2=$value1
echo The resulting value is $value2