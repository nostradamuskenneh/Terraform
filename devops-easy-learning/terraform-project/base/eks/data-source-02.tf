data "aws_ssm_parameter" "vpc-id" {
  name = join("/", ["${var.param_store_prefix_vpc}", "vpc-id"])
}

data "aws_ssm_parameter" "vpc-private-and-public-subnet-ids" {
  name = join("/", ["${var.param_store_prefix_vpc}", "vpc-private-and-public-subnet-ids"])
}

data "aws_ssm_parameter" "vpc-private-subnet-ids" {
  name = join("/", ["${var.param_store_prefix_vpc}", "vpc-private-subnet-ids"])
}

data "aws_ssm_parameter" "vpc-public-subnet-ids" {
  name = join("/", ["${var.param_store_prefix_vpc}", "vpc-public-subnet-ids"])
}

# locals {
#   vpc-private-subnet-ids            = split(",", data.aws_ssm_parameter.vpc-private-subnet-ids.value)
#   vpc-public-subnet-ids             = split(",", data.aws_ssm_parameter.vpc-public-subnet-ids.value)
#   vpc-private-and-public-subnet-ids = split(",", data.aws_ssm_parameter.vpc-private-and-public-subnet-ids.value)
# }
