##-----------Function in shell script---------
#!/bin/bash


function_name () { 
   list of commands
}


function function_name () { 
   list of commands
}


#!/bin/bash
function hello_world () {
   echo 'hello world'
}
hello_world


#!/bin/bash
hello_world () {
   echo 'hello world'
}
hello_world


#!/bin/sh
# Calling one function from another
number_one () {
   echo "This is the first function speaking..."
   number_two
}
number_two () {
   echo "This is now the second function speaking..."
}
# Calling function one.
number_one


#!/bin/sh
# Global variable
UBUNTU=`cat /etc/*release |grep ID_LIKE |awk -F= '{print$2}'`

number_one () {
   VAR="Tia"
   echo "This is the first function speaking..."
   echo "This is $UBUNTU server from function 1"
   echo "My name is $VAR from function 1"
}

number_two () {
   echo "This is now the second function speaking..."
   echo "This is $UBUNTU server from function 2"
   echo "My name is $VAR from function 2"
}

# Calling function one.
number_two
number_one