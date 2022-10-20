resource "aws_security_group" "bastion-host-sg" {
  name   = "bastion-host-sg"
  vpc_id = "vpc-0c5aaf2965a673d06"
  tags = {
    "Name" = "bastion-host-sg"
  }
}

resource "aws_security_group_rule" "bastion-host-sg-80" {
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  type              = "ingress"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.bastion-host-sg.id
}

resource "aws_security_group_rule" "outbound_rule_bastion" {
  from_port         = 0
  protocol          = "-1"
  security_group_id = aws_security_group.bastion-host-sg.id
  to_port           = 0
  type              = "egress"
  cidr_blocks       = ["0.0.0.0/0"]
}
