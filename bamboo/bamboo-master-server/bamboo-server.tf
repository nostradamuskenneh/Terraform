# EC2 Instance
resource "aws_instance" "bamboo" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t2.large" # 2cpu and 8G of ram
  user_data              = file("${path.module}/bamboo-user-data/bamboo-user-data.sh")
  key_name               = "jenkins-key"
  vpc_security_group_ids = [aws_security_group.sg.id]

  subnet_id = data.aws_subnet.db-subnet-public-01.id

  tags = {
    "Name" = "bamboo-master-server"
  }
}

# Create Elastic IP for Bastion Host
resource "aws_eip" "bamboo_eip" {
  instance = aws_instance.bamboo.id
  vpc      = true
  tags = {
    "Name" = "Bastion Pulic IP"
  }
}

resource "aws_route53_record" "cluster-alias" {
  depends_on = [aws_eip.bamboo_eip, aws_instance.bamboo]
  zone_id    = "Z09063052B43KCQ7FSGHY"
  name       = "bamboo-server"
  type       = "A"
  ttl        = "300"
  records    = [aws_eip.bamboo_eip.public_ip]
}
