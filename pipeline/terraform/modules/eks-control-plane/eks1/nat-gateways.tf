
resource "aws_nat_gateway" "gw1" {
  allocation_id = aws_eip.nat1.id
  subnet_id     = aws_subnet.public_1.id
  tags = {
    Name        = format("%s-%s-%s-nat-gateway-01", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner       = var.tags.Owner
    Access-ID   = var.tags.Access-ID
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}

resource "aws_nat_gateway" "gw2" {
  allocation_id = aws_eip.nat2.id
  subnet_id     = aws_subnet.public_2.id
  tags = {
    Name        = format("%s-%s-%s-nat-gateway-02", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner       = var.tags.Owner
    Access-ID   = var.tags.Access-ID
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}


