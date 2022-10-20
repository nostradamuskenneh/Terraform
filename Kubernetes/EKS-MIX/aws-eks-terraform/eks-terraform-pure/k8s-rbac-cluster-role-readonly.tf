# Custom RBAC Roles
resource "kubernetes_cluster_role" "pecs-cluster-role-readonly" {
  depends_on = [null_resource.cluster-auth-apply]
  metadata {
    name   = "${var.cluste_readonly_role_name_prefix}-cluster-role-${var.cluste_readonly_group_name_to_bind}"
    labels = merge(var.cluste_readonly_common_labels)
  }

  rule {
    api_groups = var.cluste_readonly_role_api_groups
    resources  = var.cluste_readonly_role_resources
    verbs      = var.cluste_readonly_role_verbs
  }
}

resource "kubernetes_cluster_role_binding" "cluster-role-binding-readonly" {
  depends_on = [kubernetes_cluster_role.pecs-cluster-role-readonly]
  count      = var.create_cluster_role_binding == "1" ? 1 : 0
  metadata {
    name   = "${var.cluste_readonly_role_name_prefix}-${var.cluste_readonly_group_name_to_bind}"
    labels = merge(var.cluste_readonly_common_labels)
  }
  role_ref {
    api_group = "rbac.authorization.k8s.io"
    kind      = "ClusterRole"
    name      = "${var.cluste_readonly_role_name_prefix}-cluster-role-${var.cluste_readonly_group_name_to_bind}"
  }
  subject {
    kind      = var.cluste_readonly_role_kind
    name      = var.cluste_readonly_group_name_to_bind
    api_group = ""
  }
}


variable "cluste_readonly_role_name_prefix" {
  type    = string
  default = "terratest-testing"
}

variable "cluste_readonly_common_labels" {
  type = map(string)
  default = {
    Environment = "dev"
    Owner       = "pecs-team"
    CreateBy    = "Terraform"
  }
}

variable "cluste_readonly_group_name_to_bind" {
  type    = string
  default = "developers-group"
}

variable "cluste_readonly_role_verbs" {
  type    = list(string)
  default = ["get", "list", "watch"]
}

variable "cluste_readonly_role_resources" {
  type    = list(string)
  default = ["namespaces", "nodes"]
}

variable "cluste_readonly_role_api_groups" {
  type    = list(string)
  default = ["*"]
}

variable "create_cluster_role_binding" {
  type    = string
  default = 1
}

variable "cluste_readonly_role_kind" {
  type    = string
  default = "Group"
}
