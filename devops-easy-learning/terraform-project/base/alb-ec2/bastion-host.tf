# # EC2 Instance
# resource "aws_instance" "bastion" {
#   ami                         = data.aws_ami.amzlinux2.id
#   instance_type               = "t2.micro"
#   user_data                   = file("${path.module}/user-data/bastion-host-user-data.sh")
#   user_data_replace_on_change = true
#   key_name                    = "jenkins-key"
#   vpc_security_group_ids      = [aws_security_group.bastion-host-sg.id]
#   associate_public_ip_address = true
#   subnet_id                   = "subnet-0890d120f106adcd3"

#   tags = {
#     "Name" = "bastion-host"
#   }
# }


# # Create Elastic IP for Bastion Host
# resource "aws_eip" "bastion_eip" {
#   instance = aws_instance.bastion.id
#   vpc      = true
#   tags = {
#     "Name" = "Bastion Pulic IP"
#   }
# }


# # Create a Null Resource and Provisioners
# resource "null_resource" "copy_ec2_keys" {
#   depends_on = [aws_instance.bastion]
#   # Connection Block for Provisioners to connect to EC2 Instance
#   connection {
#     type        = "ssh"
#     host        = aws_eip.bastion_eip.public_ip
#     user        = "ec2-user"
#     password    = ""
#     private_key = file("private-key/jenkins-key.pem")
#   }

#   ## File Provisioner: Copies the jenkins-key.pem file to /tmp/jenkins-key.pem
#   provisioner "file" {
#     source      = "private-key/jenkins-key.pem"
#     destination = "/tmp/jenkins-key.pem"
#   }
#   ## Remote Exec Provisioner: Using remote-exec provisioner fix the private key permissions on Bastion Host
#   provisioner "remote-exec" {
#     inline = [
#       "sudo chmod 400 /tmp/jenkins-key.pem"
#     ]
#   }
# }
