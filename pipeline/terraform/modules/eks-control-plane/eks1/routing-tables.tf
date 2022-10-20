resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  tags = {
    Name        = format("%s-%s-%s-public-route-table", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner       = var.tags.Owner
    Access-ID   = var.tags.Access-ID
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}

resource "aws_route_table" "private1" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.gw1.id
  }
  tags = {
    Name        = format("%s-%s-%s-private-route-table-01", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner       = var.tags.Owner
    Access-ID   = var.tags.Access-ID
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}

resource "aws_route_table" "private2" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.gw2.id
  }
  tags = {
    Name        = format("%s-%s-%s-private-route-table-02", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner       = var.tags.Owner
    Access-ID   = var.tags.Access-ID
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}
