resource "aws_instance" "app_server" {
  ami           = "ami-052efd3df9dad4825"
  instance_type = "t2.micro"

  tags = {
    Name = "web01"
  }
}

locals {
  instance_name = "web_with_local_variable"
}

resource "aws_instance" "app_server05" {
  ami           = "ami-052efd3df9dad4825"
  instance_type = var.instance_type

  tags = {
    Name = local.instance_name
  }
}

resource "aws_instance" "app_server06" {
  ami           = data.aws_ami.amzlinux.id
  instance_type = var.instance_type

  tags = {
    Name = "EC2-with-data-source"
  }
}
