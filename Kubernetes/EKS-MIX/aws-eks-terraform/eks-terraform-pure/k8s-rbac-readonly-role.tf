resource "kubernetes_role" "readonly_pecs-cluster-role" {
  depends_on = [null_resource.cluster-auth-apply]
  count      = length(var.readonly_cluster_role_name_space)
  metadata {
    name      = "${var.readonly_role_name_prefix}-role-${var.readonly_cluster_role_name_space[count.index]}"
    namespace = var.readonly_cluster_role_name_space[count.index]
    labels    = merge(var.readonly_common_labels)
  }

  rule {
    api_groups = var.readonly_role_api_groups
    resources  = var.readonly_role_resources
    verbs      = var.readonly_role_verbs
  }
}

resource "kubernetes_role_binding" "readonly_example" {
  depends_on = [kubernetes_role.pecs-cluster-role]
  count      = length(var.readonly_cluster_role_name_space)
  metadata {
    name      = "${var.readonly_role_name_prefix}-rolebinding-${var.readonly_cluster_role_name_space[count.index]}"
    namespace = var.readonly_cluster_role_name_space[count.index]
    labels    = merge(var.readonly_common_labels)
  }
  role_ref {
    api_group = "rbac.authorization.k8s.io"
    kind      = "Role"
    name      = "${var.readonly_role_name_prefix}-role-${var.readonly_cluster_role_name_space[count.index]}"
  }
  subject {
    kind      = var.readonly_role_kind
    name      = var.readonly_group_name_to_bind
    api_group = ""
    namespace = var.readonly_cluster_role_name_space[count.index]
  }
}

variable "readonly_role_name_prefix" {
  type    = string
  default = "terraform-testing"
}

variable "readonly_common_labels" {
  type = map(string)
  default = {
    Environment = "dev"
    Owner       = "pecs-team"
    CreateBy    = "Terraform"
  }
}

variable "readonly_cluster_role_name_space" {
  type = list(string)
  default = [
    "default",
    "kube-system",
    "prod",
    "qa1",
    "qa2"
  ]
}

variable "readonly_group_name_to_bind" {
  type    = string
  default = "eks-readonly-group" # "ServiceAccount", "User", "Group"
}

variable "readonly_role_verbs" {
  type    = list(string)
  default = ["get", "list", "watch"]
}

variable "readonly_role_resources" {
  type    = list(string)
  default = ["*"]
}

variable "readonly_role_api_groups" {
  type    = list(string)
  default = ["*"]
}

variable "readonly_role_kind" {
  type    = string
  default = "Group" # "ServiceAccount", "User", "Group"
}

