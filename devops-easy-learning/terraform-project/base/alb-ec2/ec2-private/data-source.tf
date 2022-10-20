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
