resource "aws_ssm_parameter" "eks-name" {
  name  = join("/", ["${var.param_store_prefix_eks}", "${aws_eks_cluster.demo.id}"])
  type  = "String"
  value = aws_eks_cluster.demo.id
  tags  = var.common_tags
}

resource "aws_ssm_parameter" "cluster-public_endpoint" {
  name  = join("/", ["${var.param_store_prefix_eks}", "${aws_eks_cluster.demo.id}-public-endpoint"])
  type  = "String"
  value = aws_eks_cluster.demo.endpoint
  tags  = var.common_tags
}
