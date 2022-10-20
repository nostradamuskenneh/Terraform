# resource "local_file" "resource-config-yaml" {
#   depends_on = [
#     null_resource.cluster-auth-apply,
#     kubernetes_namespace.k8s_namespace
#   ]
#   content  = var.resource_content
#   filename = "${var.resource_name}-${var.control_plane_name}-nginx.yaml"
# }

# resource "null_resource" "mod-apply-overwrite" {
#   depends_on = [local_file.resource-config-yaml]
#   provisioner "local-exec" {
#     command = "kubectl apply -f ${local_file.resource-config-yaml.filename} --namespace ${var.namespace}"
#   }
#   triggers = {
#     always_run = timestamp()
#   }
# }


# variable "resource_content" {
#   type    = string
#   default = <<DATA
# apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
# kind: Deployment
# metadata:
#   name: patch-demo
# spec:
#   replicas: 2
#   selector:
#     matchLabels:
#       app: nginx
#   template:
#     metadata:
#       labels:
#         app: nginx
#     spec:
#       containers:
#       - name: patch-demo-ctr
#         image: nginx
#       tolerations:
#       - effect: NoSchedule
#         key: dedicated
#         value: test-teams
# DATA
# }

# variable "resource_type" {
#   type    = string
#   default = "deployment"
# }

# variable "namespace" {
#   type    = string
#   default = "dev1"
# }

# variable "resource_name" {
#   type    = string
#   default = "nginx-test"
# }
