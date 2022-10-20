#------------------------ ECHO COMMAND DAY 01-----------------------

echo -e 'Hello, \nWorld, \nthis \nis \nPNAP!'
echo -e 'Hello, \tWorld!'

echo -e -n 'Hello, World! \nHello Tia\nI hope you are doing well'
echo -e 'Hello, World! \nHello Tia\nI hope you are doing well'

echo -e 'Hello, World! \nThis is PNAP!' >> test.txt
echo "This is the list of directories and files on this system: $(ls)"

NAME="Zara Ali"
echo $NAME
echo ${NAME}

echo "The kernel version is: `uname -r`"
echo "The kernel version is: $(uname -r)"
UNAME=`uname -r`
KERNEL=$(uname -r)
echo "The kernel version is: ${KERNEL}"
echo "The kernel version is: ${UNAME}"

echo $USER

echo $0, $1, $3, $4 .......... $9

echo -e 'Hello, \tWorld, \tthis \tvis \t\t\tPNAP!'
echo -e "List of fruits:\nOrange \t\t\tBanana \t\t\tApple \t\t\tAvocado"
echo -e '\t- Hello, \n\t- World, \n\t- this \n\t- vis \n\t- PNAP!'

echo -e "List of fruits:\n\t- Orange\n\t- Banana \n\t- Apple \n\t- Avocado"
echo -e "List of fruits:\n- Orange\n- Banana \n- Apple \n- Avocado"



#------------------------ ECHO COMMAND DAY 02-----------------------

#!/bin/bash
read -p "Enter the your first name: " FIRST_NAME 
read -p "Enter the your last name: " LAST_NAME
read -p "Enter your age: " AGE
echo "Hello $LAST_NAME! Your first name is $FIRST_NAME, your last name is $LAST_NAME and you are $AGE years old."

#!/bin/bash
echo "Enter the your first name: "
read FIRST_NAME 
echo "Enter the your last name: "
read LAST_NAME
echo "Enter your age: "
read AGE
echo "Hello $LAST_NAME! Your first name is $FIRST_NAME, your last name is $LAST_NAME and you are $AGE years old."



#!/bin/bash
read -p "Enter the your first name: " FIRST_NAME 
read -p "Enter the your last name: " LAST_NAME
read -p "Enter your age: " AGE
read -p "Enter your password: " PASSWORD
echo "Hello $LAST_NAME! Your first name is $FIRST_NAME, your last name is $LAST_NAME and you are $AGE years old. You password is $PASSWORD"

#!/bin/bash
read -p "Enter the your first name: " FIRST_NAME 
read -p "Enter the your last name: " LAST_NAME
read -p "Enter your age: " AGE
read -s -p "Enter your password: " PASSWORD
echo "Hello $LAST_NAME! Your first name is $FIRST_NAME, your last name is $LAST_NAME and you are $AGE years old. You password is $PASSWORD"


#!/bin/bash
read -p "Enter the your first name: " FIRST_NAME 
read -p "Enter the your last name: " LAST_NAME
read -p "Enter your age: " AGE
read -s -p "Enter your password: " PASSWORD

echo -e "Hello $LAST_NAME! \nYour first name is :$FIRST_NAME \nYour last name is: $LAST_NAME \nYou are $AGE years old \nYou password is: $PASSWORD"


#!/bin/bash
read -p "Enter the your first name: " FIRST_NAME 
read -p "Enter the your last name: " LAST_NAME
read -p "Enter your age: " AGE
read -s -p "Enter your password: " PASSWORD

echo -e "Hello $LAST_NAME! \n
Your first name is :$FIRST_NAME \n
Your last name is: $LAST_NAME \n
You are $AGE years old \n
You password is: $PASSWORD"


#!/bin/bash
read -p "Enter the your first name: " FIRST_NAME 
read -p "Enter the your last name: " LAST_NAME
read -p "Enter your age: " AGE
read -s -p "Enter your password: " PASSWORD

useradd $FIRST_NAME  
usermod -c "$FIRST_NAME $LAST_NAME" $FIRST_NAME
cat /etc/passwd |grep $FIRST_NAME 



#------------------------ ECHO COMMAND DAY 03-----------------------
#!/bin/bash
echo "The name of the your computer is: $HOSTNAME"
echo "Your home directory is: $PWD"
echo "Your present working directory is: $HOME"
echo "The Shell being used by the user: $SHELL"
echo "The user who is currently login is: $USER"
echo "The user ID is: $ID"

echo "The kernel version is: `uname -r`"
echo "The kernel version is: $(uname -r)"
echo -e "Date and calendar: \n `date` \n `cal`"

#!/bin/bash
cat << EOF
  The name of the your computer is: $HOSTNAME
  Your home directory is: $PWD"
  Your present working directory is: $HOME
  The Shell being used by the user: $SHELL
  The user who is currently login is: $USER
  The user ID is: $ID"

  The kernel version is: `uname -r`
  The kernel version is: $(uname -r)
EOF


#!/bin/bash
cat << A
  The name of the your computer is: $HOSTNAME
  Your home directory is: $PWD"
  Your present working directory is: $HOME
  The Shell being used by the user: $SHELL
  The user who is currently login is: $USER
  The user ID is: $ID"

  The kernel version is: `uname -r`
  The kernel version is: $(uname -r)
A

echo -e "
  The name of the your computer is: $HOSTNAME
  Your home directory is: $PWD
  Your present working directory is: $HOME
  The Shell being used by the user: $SHELL
  The user who is currently login is: $USER
  The user ID is: $ID

  The kernel version is: `uname -r`
  The kernel version is: $(uname -r)
"

#!/bin/bash
echo
cat << EOF
- This concept is useful to write simple and short shell scripts.
- Chaining of Linux commands means, combining several commands and make them execute based upon the behavior of operator used in between them.
- The different Command Chaining Operators are:
    - Semi-colon Operator ;
    - Logical AND Operators &&
    - Logical OR Operator ||
    - Logical AND - OR Operators && ||
EOF
echo
ls -l



