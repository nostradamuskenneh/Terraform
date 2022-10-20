resource "kubernetes_role" "pecs-cluster-role" {
  depends_on = [
    null_resource.cluster-auth-apply,
    kubernetes_namespace.k8s_namespace
  ]
  count = length(var.cluster_role_name_space)
  metadata {
    name      = "${var.role_name_prefix}-readonly-role-${var.cluster_role_name_space[count.index]}"
    namespace = var.cluster_role_name_space[count.index]
    labels    = merge(var.common_labels)
  }

  rule {
    api_groups = var.role_api_groups
    resources  = var.role_resources
    verbs      = var.role_verbs
  }
}

resource "kubernetes_role_binding" "example" {
  depends_on = [
    kubernetes_role.pecs-cluster-role,
    kubernetes_namespace.k8s_namespace
  ]
  count = length(var.cluster_role_name_space)
  metadata {
    name      = "${var.role_name_prefix}-readonly-rolebinding-${var.cluster_role_name_space[count.index]}"
    namespace = var.cluster_role_name_space[count.index]
    labels    = merge(var.common_labels)
  }
  role_ref {
    api_group = "rbac.authorization.k8s.io"
    kind      = "Role"
    name      = "${var.role_name_prefix}-readonly-role-${var.cluster_role_name_space[count.index]}"
  }
  subject {
    kind      = var.role_kind
    name      = var.user_name_to_bind
    api_group = ""
    namespace = var.cluster_role_name_space[count.index]
  }
}

variable "role_name_prefix" {
  type    = string
  default = "terraform-testing"
}

variable "common_labels" {
  type = map(string)
  default = {
    Environment = "dev"
    Owner       = "pecs-team"
    CreateBy    = "Terraform"
  }
}

variable "cluster_role_name_space" {
  type = list(string)
  default = [
    "default",
    "kube-system"
  ]
}

variable "user_name_to_bind" {
  type    = string
  default = "eks-admin" # "ServiceAccount", "User", "Group"
}

variable "role_verbs" {
  type    = list(string)
  default = ["get", "list", "watch", "create", "delete"]
}

variable "role_resources" {
  type    = list(string)
  default = ["*"]
}

variable "role_api_groups" {
  type    = list(string)
  default = ["*"]
}

variable "role_kind" {
  type    = string
  default = "User" # "ServiceAccount", "User", "Group"
}

