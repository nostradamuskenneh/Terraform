data "aws_vpc" "adl_eks_vpc" {
  filter {
    name   = "tag:Name"
    values = ["adl-eks-vpc"]
  }
}

data "aws_subnet" "eks_private_subnet_01" {
  filter {
    name   = "tag:Name"
    values = ["eks-private-subnet-01"]
  }
}


data "aws_subnet" "eks_private_subnet_02" {
  filter {
    name   = "tag:Name"
    values = ["eks-private-subnet-02"]
  }
}


data "aws_subnet" "eks_public_subnet_01" {
  filter {
    name   = "tag:Name"
    values = ["eks-public-subnet-01"]
  }
}

data "aws_subnet" "eks_public_subnet_02" {
  filter {
    name   = "tag:Name"
    values = ["eks-public-subnet-02"]
  }
}

