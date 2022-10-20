resource "aws_iam_role" "nodes_general" {
  name = format("%s-%s-%s-eks-node-group-iam-role", var.tags.Access-ID, var.tags.Project, var.tags.Environment)

  assume_role_policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      }, 
      "Action": "sts:AssumeRole"
    }
  ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "amazon_eks_worker_node_policy_general" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role       = aws_iam_role.nodes_general.name
}

resource "aws_iam_role_policy_attachment" "amazon_eks_cni_policy_general" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role       = aws_iam_role.nodes_general.name
}

resource "aws_iam_role_policy_attachment" "amazon_ec2_container_registry_read_only" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role       = aws_iam_role.nodes_general.name
}

resource "aws_eks_node_group" "nodes_general" {
  cluster_name    = aws_eks_cluster.eks.name
  node_group_name = format("%s-%s-%s-eks-node-group-name", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
  node_role_arn   = aws_iam_role.nodes_general.arn

  subnet_ids = [
    aws_subnet.private_1.id,
    aws_subnet.private_2.id
  ]

  scaling_config {
    desired_size = var.node-group-desired-size
    max_size     = var.node-group-max-size
    min_size     = var.node-group-min-size
  }

  ami_type = "AL2_x86_64"
  # capacity_type = "ON_DEMAND"
  disk_size = var.node-group-disk-size

  force_update_version = false
  instance_types       = var.eks-node-group-instance-types

  labels = {
    role = format("%s-%s-%s-eks-node-group-role", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
  }
  version = var.eks-node-group-version
  depends_on = [
    aws_iam_role_policy_attachment.amazon_eks_worker_node_policy_general,
    aws_iam_role_policy_attachment.amazon_eks_cni_policy_general,
    aws_iam_role_policy_attachment.amazon_ec2_container_registry_read_only,
  ]
}
