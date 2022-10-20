resource "kubernetes_cluster_role_v1" "eksreadonly_clusterrole" {
  metadata {
    name = "eksreadonly-clusterrole"
  }
  rule {
    api_groups = [""] # These come under core APIs
    resources  = ["*"]
    verbs      = ["get", "list"]
  }
  rule {
    api_groups = ["apps"]
    resources  = ["*"]
    verbs      = ["get", "list"]
  }
  rule {
    api_groups = ["batch"]
    resources  = ["*"]
    verbs      = ["get", "list"]
  }
}
