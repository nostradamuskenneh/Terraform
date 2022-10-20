resource "null_resource" "cluster-auth-apply" {
  provisioner "local-exec" {
    command = "aws eks update-kubeconfig --name ${var.control_plane_name} --region ${var.aws_region}"
  }
  triggers = {
    always_run = timestamp()
  }
}

