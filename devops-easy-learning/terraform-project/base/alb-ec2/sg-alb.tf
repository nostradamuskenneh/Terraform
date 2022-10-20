resource "aws_security_group" "alb-webserver-sg" {
  name   = "alb-webserver-sg"
  vpc_id = "vpc-0c5aaf2965a673d06"
  tags = {
    "Name" = "alb-webserver-sg"
  }
}

resource "aws_security_group_rule" "alb-webserver-sg-80" {
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  type              = "ingress"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.alb-webserver-sg.id
}

resource "aws_security_group_rule" "alb-webserver-sg-443" {
  from_port         = 443
  to_port           = 443
  protocol          = "tcp"
  type              = "ingress"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.alb-webserver-sg.id
}

resource "aws_security_group_rule" "outbound_rule_alb" {
  from_port         = 0
  protocol          = "-1"
  security_group_id = aws_security_group.alb-webserver-sg.id
  to_port           = 0
  type              = "egress"
  cidr_blocks       = ["0.0.0.0/0"]
}
