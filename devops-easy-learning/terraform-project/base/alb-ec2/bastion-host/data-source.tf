# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/vpcs

# data "aws_vpc" "adl_eks_vpc" {
#   tags = {
#     Name = "adl-eks-vpc"
#   }
# }

# data "aws_subnet" "eks_public_subnet_01" {
#   tags = {
#     Name = "eks-public-subnet-01"
#   }
# }


# https://wahlnetwork.com/2020/04/30/filter-terraform-data-source-by-aws-tag-value/

# https://www.youtube.com/watch?v=9cDDZzl7zow

data "aws_vpc" "adl_eks_vpc" {
  filter {
    name   = "tag:Name"
    values = ["adl-eks-vpc"]
  }
}

data "aws_subnet" "eks_public_subnet_01" {
  filter {
    name   = "tag:Name"
    values = ["eks-public-subnet-01"]
  }
}


