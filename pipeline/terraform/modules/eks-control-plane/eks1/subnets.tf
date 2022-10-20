resource "aws_subnet" "public_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.vpc-public-subnets[0]
  availability_zone       = var.availability-zones[0]
  map_public_ip_on_launch = true
  tags = {
    Name                              = format("%s-%s-%s-public-subnet-01", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner                             = var.tags.Owner
    Access-ID                         = var.tags.Access-ID
    Project                           = var.tags.Project
    Environment                       = var.tags.Environment
    Create_By                         = var.tags.Create_By
    "kubernetes.io/cluster/eks"       = "shared"
    "kubernetes.io/role/internal-elb" = 1
  }
}

resource "aws_subnet" "public_2" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.vpc-public-subnets[1]
  availability_zone       = var.availability-zones[1]
  map_public_ip_on_launch = true
  tags = {
    Name                              = format("%s-%s-%s-public-subnet-02", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner                             = var.tags.Owner
    Access-ID                         = var.tags.Access-ID
    Project                           = var.tags.Project
    Environment                       = var.tags.Environment
    Create_By                         = var.tags.Create_By
    "kubernetes.io/cluster/eks"       = "shared"
    "kubernetes.io/role/internal-elb" = 1
  }
}

resource "aws_subnet" "private_1" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.vpc-private-subnets[0]
  availability_zone = var.availability-zones[0]
  tags = {
    Name                              = format("%s-%s-%s-private-subnet-01", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner                             = var.tags.Owner
    Access-ID                         = var.tags.Access-ID
    Project                           = var.tags.Project
    Environment                       = var.tags.Environment
    Create_By                         = var.tags.Create_By
    "kubernetes.io/cluster/eks"       = "shared"
    "kubernetes.io/role/internal-elb" = 1
  }
}

resource "aws_subnet" "private_2" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.vpc-private-subnets[1]
  availability_zone = var.availability-zones[1]
  tags = {
    Name                              = format("%s-%s-%s-private-subnet-02", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner                             = var.tags.Owner
    Access-ID                         = var.tags.Access-ID
    Project                           = var.tags.Project
    Environment                       = var.tags.Environment
    Create_By                         = var.tags.Create_By
    "kubernetes.io/cluster/eks"       = "shared"
    "kubernetes.io/role/internal-elb" = 1
  }
}
