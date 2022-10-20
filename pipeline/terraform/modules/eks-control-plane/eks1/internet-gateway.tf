resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name        = format("%s-%s-%s-internet-gateway", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner       = var.tags.Owner
    Access-ID   = var.tags.Access-ID
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}
