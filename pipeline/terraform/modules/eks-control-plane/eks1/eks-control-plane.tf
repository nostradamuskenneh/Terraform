resource "aws_iam_role" "eks_cluster_assume_role" {
  name               = format("%s-%s-%s-cluster-assume-role", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "eks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "amazon_eks_cluster_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.eks_cluster_assume_role.name
}

resource "aws_eks_cluster" "eks" {
  name     = format("%s-%s-%s-eks-control-plane", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
  role_arn = aws_iam_role.eks_cluster_assume_role.arn
  version  = var.eks-control-plane-version

  vpc_config {
    endpoint_private_access = false
    endpoint_public_access  = true

    subnet_ids = [
      aws_subnet.public_1.id,
      aws_subnet.public_2.id,
      aws_subnet.private_1.id,
      aws_subnet.private_2.id
    ]
  }

  depends_on = [
    aws_iam_role_policy_attachment.amazon_eks_cluster_policy
  ]
}
