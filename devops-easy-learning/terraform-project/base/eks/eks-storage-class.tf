# resource "kubernetes_storage_class" "aws-gp2-storage-class" {
#   metadata {
#     name = "aws-gp2-storage-class"
#     annotations = {
#       "storageclass.kubernetes.io/is-default-class" = "false"
#     }
#   }
#   allow_volume_expansion = "true"
#   volume_binding_mode    = "WaitForFirstConsumer"
#   reclaim_policy         = "Delete"
#   storage_provisioner    = "kubernetes.io/aws-ebs"
#   depends_on = [
#     aws_eks_cluster.demo
#   ]
#   parameters = {
#     type   = "gp2"
#     fsType = "ext4"
#   }
# }
