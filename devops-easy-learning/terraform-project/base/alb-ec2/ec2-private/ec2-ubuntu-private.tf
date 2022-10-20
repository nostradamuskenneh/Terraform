# EC2 Instance
resource "aws_instance" "ec2-private" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.micro"
  key_name               = "jenkins-key"
  vpc_security_group_ids = [aws_security_group.ssh_http_sg.id]

  subnet_id = data.aws_subnet.eks_private_subnet_01.id

  tags = {
    "Name" = "ec2-private"
  }
}

