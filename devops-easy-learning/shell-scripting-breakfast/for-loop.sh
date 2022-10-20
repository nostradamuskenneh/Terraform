echo "#########################FOR LOOP############## CAN ONLY RUN ON UBUNTU###############"

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

read -p "select enter one or more package from the list above above: " PACKAGE

for i in $PACKAGE 
do 
echo "installing $i"
apt install -y $i
done 




cat <<EOF > print.sh
wget 
curl 
vim 
unzip 
tree 
git 
default-jre 
default-jdk 
firewalld 
python3-pip 
ansible 
nodejs 
make 
build-essential 
npm 
ufw
apt-utils
EOF

read -p "Do you wan to install all packages mention above enter yes or no: " QUESTION

if 
[[ $QUESTION == yes ]]
then 
    for i in $(cat print.sh)
    do
    echo "installing $i"
    apt install -y $i 
    done
fi 

clear 

if [[ $QUESTION == yes ]]
then 
    echo "ckecking"
    for j in $(cat print.sh)
    do 
    which $j
    done
fi 


############adding all user

USER=$(cat user.txt)

for l in $USER 
do 
useradd -m -d /home/$l  $l
done 