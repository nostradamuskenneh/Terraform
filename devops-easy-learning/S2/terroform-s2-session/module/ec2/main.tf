# provider "aws" {
#   region = "us-east-1"
# }


resource "aws_instance" "myec3" {
  ami           = data.aws_ami.amzlinux.id
  instance_type = var.instance_type
  key_name      = var.instance_key

  tags = {
    "Name" = "${var.instance_name}-web01"
    "Env"  = var.env
  }
}
