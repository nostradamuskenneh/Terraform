
variable "node_max" {
  type    = string
  default = "5"
}

variable "node_min" {
  type    = string
  default = "1"
}

variable "desired_node" {
  type    = string
  default = "1"
}

variable "blue_node_color" {
  type    = string
  default = "blue"
}

variable "green_node_color" {
  type    = string
  default = "green"
}

variable "blue" {
  type    = bool
  default = false
}

variable "green" {
  type    = bool
  default = false
}


locals {
  vpc-private-subnet-ids            = split(",", data.aws_ssm_parameter.vpc-private-subnet-ids.value)
  vpc-public-subnet-ids             = split(",", data.aws_ssm_parameter.vpc-public-subnet-ids.value)
  vpc-private-and-public-subnet-ids = split(",", data.aws_ssm_parameter.vpc-private-and-public-subnet-ids.value)
}

resource "aws_eks_node_group" "green-nodes" {
  cluster_name    = aws_eks_cluster.demo.name
  node_group_name = "${var.control_plane_name}-eks-green-node-group"
  node_role_arn   = aws_iam_role.nodes.arn
  subnet_ids = [
    local.vpc-public-subnet-ids[0],
    local.vpc-public-subnet-ids[1]
  ]
  capacity_type = "ON_DEMAND"
  ami_type      = "AL2_x86_64"
  instance_types = [
    "t3.medium",
    # "t3.small",
    # "t2.micro"
  ]
  disk_size = 20
  remote_access {
    ec2_ssh_key = "jenkins-key"
  }
  scaling_config {
    desired_size = var.green_node_color == "green" && var.green ? var.desired_node : 0
    min_size     = var.green_node_color == "green" && var.green ? var.node_min : 0
    max_size     = var.green_node_color == "green" && var.green ? var.node_max : var.node_max
  }
  update_config {
    max_unavailable = 1
  }
  labels = {
    "deployment.nodegroup" = "green"
  }
  version = "1.21"

  depends_on = [
    aws_iam_role_policy_attachment.nodes-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.nodes-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.nodes-AmazonEC2ContainerRegistryReadOnly,
  ]

  tags = {
    Name                                                  = "${var.control_plane_name} EKS Public-Node-Group"
    "k8s.io/cluster-autoscaler/${var.control_plane_name}" = "owned"
    "k8s.io/cluster-autoscaler/enabled "                  = "true"
  }
}


resource "aws_eks_node_group" "blue-nodes" {
  cluster_name    = aws_eks_cluster.demo.name
  node_group_name = "${var.control_plane_name}-eks-blue-node-group"
  node_role_arn   = aws_iam_role.nodes.arn
  subnet_ids = [
    local.vpc-public-subnet-ids[0],
    local.vpc-public-subnet-ids[1]
  ]
  capacity_type = "ON_DEMAND"
  ami_type      = "AL2_x86_64"
  instance_types = [
    "t3.medium",
    # "t3.small",
    # "t2.micro"
  ]
  disk_size = 20
  remote_access {
    ec2_ssh_key = "jenkins-key"
  }

  scaling_config {
    desired_size = var.blue_node_color == "blue" && var.blue ? var.desired_node : 0
    min_size     = var.blue_node_color == "blue" && var.blue ? var.node_min : 0
    max_size     = var.blue_node_color == "blue" && var.blue ? var.node_max : var.node_max
  }
  update_config {
    max_unavailable = 1
  }
  labels = {
    "deployment.nodegroup" = "blue"
  }
  version = "1.21"

  depends_on = [
    aws_iam_role_policy_attachment.nodes-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.nodes-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.nodes-AmazonEC2ContainerRegistryReadOnly,
  ]

  tags = {
    Name                                                  = "${var.control_plane_name} EKS Public-Node-Group"
    "k8s.io/cluster-autoscaler/${var.control_plane_name}" = "owned"
    "k8s.io/cluster-autoscaler/enabled "                  = "true"
  }
}
















