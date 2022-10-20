# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_cluster

resource "aws_eks_cluster" "demo" {
  name = var.control_plane_name

  # The Amazon Resource Name (ARN) of the IAM role that provides permissions for 
  # the Kubernetes control plane to make calls to AWS API operations on your behalf
  role_arn = aws_iam_role.demo.arn

  # Desired Kubernetes master version
  # https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html
  version = "1.21"

  vpc_config {
    # Indicates whether or not the Amazon EKS private API server endpoint is enabled. 
    # This is createby default if you don't define it
    endpoint_private_access = false

    # Indicates whether or not the Amazon EKS public API server endpoint is enabled
    # This is createby default if you don't define it
    endpoint_public_access = true

    # Open the public EKS public enpoint to the entire world
    public_access_cidrs = ["0.0.0.0/0"]

    # Must be in at least two different availability zones. These subnets will be used to create load balancers and nodes by EKS
    subnet_ids = [
      data.aws_subnet.eks_private_subnet_01.id,
      data.aws_subnet.eks_private_subnet_02.id,
      # data.aws_subnet.eks_private_subnet_01.id,
      # data.aws_subnet.eks_private_subnet_02.id
    ]

    security_group_ids = [
      aws_security_group.control-plane-sg.id,
    ]

  }

  # kubernetes_network_config {
  #   service_ipv4_cidr = "172.20.0.0/16"
  # }

  # Enable EKS Cluster Control Plane Logging
  # This is helpfull for troubleshooting. We can directly see the logs of those components in AWS CloudWash when the EKS control plane is created
  enabled_cluster_log_types = [
    "api",
    "audit",
    "authenticator",
    "controllerManager",
    "scheduler"
  ]

  # Ensure that IAM Role permissions are created before and deleted after EKS Cluster handling.
  # Otherwise, EKS will not be able to properly delete EKS managed EC2 infrastructure such as Security Groups.
  # Create these resources first before creating the EKS control plane
  depends_on = [
    aws_iam_role_policy_attachment.demo-AmazonEKSClusterPolicy,
    aws_iam_role_policy_attachment.demo-AmazonEKSVPCResourceController,
  ]

  tags = {
    Name = "${var.control_plane_name} EKS Cluster"
  }
}

