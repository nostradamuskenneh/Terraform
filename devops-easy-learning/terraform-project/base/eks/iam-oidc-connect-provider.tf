
# # https://github.com/hashicorp/terraform-provider-aws/issues/10104
# resource "aws_iam_openid_connect_provider" "oidc_enable" {
#   client_id_list  = ["sts.amazonaws.com"]
#   thumbprint_list = [lower(var.oidc_thumbprint)]
#   url             = aws_eks_cluster.demo.identity.0.oidc.0.issuer
# }


# https://stackoverflow.com/questions/64624411/terraform-external-data-source-eks-thumbprint-not-working-sometimes

# openid connect provider is needed for kubernetes service account
data "tls_certificate" "example" {
  url = aws_eks_cluster.demo.identity.0.oidc.0.issuer
}

resource "aws_iam_openid_connect_provider" "example" {
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = [data.tls_certificate.example.certificates.0.sha1_fingerprint]
  url             = aws_eks_cluster.demo.identity.0.oidc.0.issuer

  tags = {
    "key" = "${var.control_plane_name} iam openid connect provider"
  }
}

output "thumbprint_hash" {
  value = data.tls_certificate.example.certificates.0.sha1_fingerprint
}


# variable "eks_oidc_root_ca_thumbprint" {
#   type        = string
#   description = "Thumbprint of Root CA for EKS OIDC, Valid until 2037"
#   default     = "9e99a48a9960b14926bb7f3b02e22da2b0ab7280"
# }


