
resource "aws_security_group" "sg" {
  name        = var.sg_name
  description = var.sg_desc
  vpc_id      = var.vpc_id
  tags        = var.common_tags
}

resource "aws_security_group_rule" "inbound" {
  count             = length(var.ports_in)
  type              = "ingress"
  from_port         = var.ports_in[count.index]
  to_port           = var.ports_in[count.index]
  protocol          = var.sg_protocol
  cidr_blocks       = var.cidrs_in
  security_group_id = aws_security_group.sg.id
}

resource "aws_security_group_rule" "outbound" {
  count             = var.include_egress == "1" ? length(var.ports_out) : 0
  type              = "egress"
  from_port         = var.ports_out[count.index]
  to_port           = var.ports_out[count.index]
  protocol          = var.sg_protocol
  cidr_blocks       = var.cidrs_out
  security_group_id = aws_security_group.sg.id
}

resource "aws_security_group_rule" "egress" {
  count             = var.include_egress == "0" ? 1 : 0
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = -1
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg.id
}

resource "aws_security_group_rule" "ping" {
  count             = var.inbound_ping ? 1 : 0
  type              = "ingress"
  from_port         = 8
  to_port           = 0
  protocol          = "icmp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.sg.id
}
