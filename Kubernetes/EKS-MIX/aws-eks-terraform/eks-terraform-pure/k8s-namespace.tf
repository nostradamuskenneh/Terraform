resource "kubernetes_namespace" "k8s_namespace" {
  depends_on = [null_resource.cluster-auth-apply]
  for_each   = toset(var.name_spaces)
  metadata {
    name = each.key
  }
}

variable "name_spaces" {
  type = list(string)
  default = [
    "monitoring",
    "jenkins",
    "sonarqube",
    "grafana",
    "dev1",
    "dev2",
    "prod",
    "stage",
    "qa1",
    "qa2"
  ]
}
