# # Resource: aws_eks_node_group
# # https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_node_group

# resource "aws_eks_node_group" "private-green-nodes" {
#   # Name of the EKS Cluster. This will associate the cluster with the node group
#   cluster_name = aws_eks_cluster.demo.name

#   # Name of the EKS Node Group.
#   node_group_name = "${var.control_plane_name}-eks-private-green-node-group"

#   # Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
#   node_role_arn = aws_iam_role.nodes.arn

#   # Identifiers of EC2 Subnets to associate with the EKS Node Group. 
#   # These subnets must have the following resource tag: kubernetes.io/cluster/CLUSTER_NAME = "owned" or "shared"
#   # (where CLUSTER_NAME is replaced with the name of the EKS Cluster).
#   subnet_ids = [
#     data.aws_subnet.eks_private_subnet_01.id,
#     data.aws_subnet.eks_private_subnet_02.id
#   ]

#   # Type of capacity associated with the EKS Node Group. 
#   # Valid values: ON_DEMAND, SPOT. Spot instances can be taking by AWS at anytime
#   # https://docs.aws.amazon.com/eks/latest/APIReference/API_Nodegroup.html
#   # ON_DEMAND is recommened for production work load
#   capacity_type = "ON_DEMAND"

#   # Type of Amazon Machine Image (AMI) associated with the EKS Node Group.
#   # Valid values:AL2_x86_64 | AL2_x86_64_GPU | AL2_ARM_64 | CUSTOM | BOTTLEROCKET_ARM_64 | BOTTLEROCKET_x86_64
#   # https://docs.aws.amazon.com/eks/latest/APIReference/API_Nodegroup.html
#   ami_type = "AL2_x86_64"

#   # List of instance types associated with the EKS Node Group
#   instance_types = [
#     # "t3.medium",
#     # "t3.small",
#     "t2.micro"
#   ]

#   # Disk size in GiB for worker nodes
#   disk_size = 20

#   # The key to login
#   remote_access {
#     ec2_ssh_key = "jenkins-key"
#   }

#   scaling_config {
#     # Desired number of worker nodes.
#     desired_size = 0

#     # Minimum number of worker nodes.
#     min_size = 0

#     # Maximum number of worker nodes.
#     max_size = 2
#   }


#   # This is the max_unailable worker nodes during a node group update
#   update_config {
#     max_unavailable = 1
#     #max_unavailable_percentage = 50    # ANY ONE TO USE
#   }

#   # create a label for the group. We can later on deploy resource on this node group using this label. 
#   #We can use affinity or node selector here to deploy a resource on a specific node group
#   labels = {
#     "deployment.nodegroup" = "green"
#   }

#   # Kubernetes version
#   # https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html
#   version = "1.21"

#   # Only pod that can tolerate the taint will be deploy on this nodes or node group
#   # taint {
#   #   key    = "team"
#   #   value  = "devops"
#   #   effect = "NO_SCHEDULE"
#   # }

#   # Ensure that IAM Role permissions are created before and deleted after EKS Node Group handling.
#   # Otherwise, EKS will not be able to properly delete EC2 Instances and Elastic Network Interfaces.
#   depends_on = [
#     aws_iam_role_policy_attachment.nodes-AmazonEKSWorkerNodePolicy,
#     aws_iam_role_policy_attachment.nodes-AmazonEKS_CNI_Policy,
#     aws_iam_role_policy_attachment.nodes-AmazonEC2ContainerRegistryReadOnly,
#   ]

#   # private node group tag
#   tags = {
#     Name = "${var.control_plane_name} EKS Private Green Node Group"

#     # This 2 tags are for cluster austoscaler. Austoscaler will not work without these 2 tags
#     "k8s.io/cluster-autoscaler/${var.control_plane_name}" = "owned"
#     "k8s.io/cluster-autoscaler/enabled "                  = "true"
#   }
# }






















