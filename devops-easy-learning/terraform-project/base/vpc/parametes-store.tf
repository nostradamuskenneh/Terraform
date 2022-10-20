resource "aws_ssm_parameter" "vpc-id" {
  name  = join("/", ["${var.vpc_prefix}", "vpc-id"])
  type  = "String"
  value = aws_vpc.main.id
  tags  = var.common_tags
}

resource "aws_ssm_parameter" "vpc-public-subnet-ids" {
  name  = join("/", ["${var.vpc_prefix}", "vpc-public-subnet-ids"])
  type  = "String"
  value = join(",", ["${aws_subnet.eks-public-subnet-01.id}", "${aws_subnet.eks-public-subnet-02.id}"])
  tags  = var.common_tags
}

resource "aws_ssm_parameter" "vpc-private-subnet-ids" {
  name  = join("/", ["${var.vpc_prefix}", "vpc-private-subnet-ids"])
  type  = "String"
  value = join(",", ["${aws_subnet.eks-private-subnet-01.id}", "${aws_subnet.eks-private-subnet-02.id}"])
  tags  = var.common_tags
}

resource "aws_ssm_parameter" "vpc-private-and-public-subnet-ids" {
  name = join("/", ["${var.vpc_prefix}", "vpc-private-and-public-subnet-ids"])
  type = "String"
  value = join(",", [
    "${aws_subnet.eks-private-subnet-01.id}",
    "${aws_subnet.eks-private-subnet-02.id}",
    "${aws_subnet.eks-public-subnet-01.id}",
    "${aws_subnet.eks-public-subnet-02.id}"

  ])
  tags = var.common_tags
}
