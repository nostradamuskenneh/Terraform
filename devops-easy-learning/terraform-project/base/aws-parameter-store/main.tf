resource "aws_ssm_parameter" "db-username" {
  name  = join("/", ["${var.param_store_prefix}", "db-username"])
  type  = "String"
  value = "admin"
  tags  = var.common_tags
}

resource "aws_ssm_parameter" "db-password" {
  name  = join("/", ["${var.param_store_prefix}", "db-password"])
  type  = "SecureString"
  value = "db-password"
  tags  = var.common_tags
}
