
resource "aws_security_group" "sg" {
  name_prefix = "ssh-sg"
  description = "Allow all inbound traffic from port 22 and 80"
  vpc_id      = data.aws_vpc.bamboo_vpc.id

  tags = {
    Name = "SSH and HTTP SG"
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_security_group_rule" "allow_all_ssh" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg.id
}

resource "aws_security_group_rule" "allow_8085" {
  type              = "ingress"
  from_port         = 8085 #to access bamboo. it runs on port 8085
  to_port           = 8085
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg.id
}

resource "aws_security_group_rule" "allow_54663" {
  type              = "ingress"
  from_port         = 54663 # agent will use this port to connect to master
  to_port           = 54663
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg.id
}

resource "aws_security_group_rule" "allow_54667" {
  type              = "ingress"
  from_port         = 54667 # agent will use this port to connect to master
  to_port           = 54667
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg.id
}

resource "aws_security_group_rule" "allow_all_ping" {
  type              = "ingress"
  from_port         = 8
  to_port           = 0
  protocol          = "icmp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg.id
}

resource "aws_security_group_rule" "allow_all_outbound" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg.id
}
