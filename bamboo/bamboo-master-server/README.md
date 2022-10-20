## Bamboo server Installation & overview
- https://www.youtube.com/watch?v=f5Z1G0Fw25c
- https://confluence.atlassian.com/bamboo/running-the-setup-wizard-289276851.html


## Steps to Install & Configure Bamboo on Ubuntu 20.04 LTS
- https://www.hackerxone.com/2022/02/11/steps-to-install-configure-bamboo-on-ubuntu-20-04-lts/
- https://www.youtube.com/watch?v=f5Z1G0Fw25c
- https://confluence.atlassian.com/bamboo/installing-bamboo-on-linux-289276792.html

## Get the Trial License
- https://my.atlassian.com/license/evaluation?_ga=2.33993189.591460940.1529673412-1332576115.1523517645
- https://my.atlassian.com/products/index?sen=18752459&evalId=18752459&eval=true#license_18752459

## Licenses
AAABwg0ODAoPeNqNkttum0AQhu/3KZB606oiWcCHxNJKxYBjKxhcoGlr+WbBY0wLC9kFJ/Tpy8lxW
qVS73YOmv3/b+adT0vJh0JSRxLWZhqeYUUyzEBSsaqin1A/ABdJzogywXiKbzRNQSHNwjy/spMIm
ABrn5Rtg+UElrfxVr6FjJyVNCodmgFJ2CH/tIdTXgigok6Bcpaw+CrKs/Mgp8pC4O5h3oV2HtFUj
4GVgsgvn5m0pEaTA05KXgHaVDw6UgFNHkirVca3sjpCZ1HPRcLrS1HBbXHQZa1pkv6PsKY3OUH/o
Q/8BHxlkvnd2JPx6Ps32cSTqeybD5O3jXiQ5SUMThSMMUp7cUsqjmRtPBmLu8e9U4ntcbv0QVHDu
ants6NzvRBloR8/L35sn9yPceYa4X3+5ddX9XpT88dA92J9R3YE+VUoIp4UHf5O5Js6Nillr1EOi
IK6gG5DhrteW56x0m3UgGkQM8qifxAcRvgl5e0qDjQVcGbesLFXpm85sq3cTMfqaHyLmoj8mXF5T
FkiaH8z91JgGUtkcOgSf29zAHa+QRWZcHHcu5Pet6ch9bfxYTeTrBNNq24aujx7PL8BnKv7TjAtA
hRq+cNyEvutFPclda52mGLsPL31zAIVAJZIl4Xv2/Kra7/oQOHBIqdPe7L7X02lh


## Server connection
```
ssh -i "jenkins-key.pem" ubuntu@ec2-44-210-207-120.compute-1.amazonaws.com

ssh -i "jenkins-key.pem" ubuntu@bamboo-server.devopseasylearning.net

ssh tia@bamboo-server.devopseasylearning.net
vim /etc/ssh/sshd_config
PasswordAuthentication no
sudo service ssh restart
```

## Connection
- bamboo = database
- bamboo-cicd-db.cv3uwkomseya.us-east-1.rds.amazonaws.com = db enpoint
```
bamboo-cicd-db.cv3uwkomseya.us-east-1.rds.amazonaws.com
jdbc:postgresql://localhost:5432/bamboo

jdbc:postgresql://bamboo-cicd-db.cv3uwkomseya.us-east-1.rds.amazonaws.com:5432/bamboo
```