
resource "local_file" "storage_class-resource-config-yaml" {
  depends_on = [
    null_resource.cluster-auth-apply,
    kubernetes_namespace.k8s_namespace
  ]
  content  = var.storage_class_resource_content
  filename = "${var.storage_class_resource_type}-${var.control_plane_name}.yaml"
}

resource "null_resource" "mod-apply-overwrite" {
  depends_on = [local_file.storage_class-resource-config-yaml]
  provisioner "local-exec" {
    command = "kubectl apply -f ${local_file.storage_class-resource-config-yaml.filename}"
  }
}

variable "storage_class_resource_content" {
  type    = string
  default = <<DATA
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: aws-gp2-storage
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4
reclaimPolicy: Retain
allowVolumeExpansion: true
mountOptions:
  - debug
volumeBindingMode: Immediate
DATA
}

variable "storage_class_resource_type" {
  type    = string
  default = "storage-class"
}





