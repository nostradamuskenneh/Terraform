resource "aws_secretsmanager_secret" "rds_password" {
  name        = "${var.secret-manager-prefix}/databases-password"
  description = "databases password"
  tags = {
    "Terraform" = "true"
    "Project"   = "ADL"
  }
}

resource "aws_secretsmanager_secret" "rds_username" {
  name        = "${var.secret-manager-prefix}/databases-username"
  description = "Username for DB"
  tags = {
    "Terraform" = "true"
    "Project"   = "ADL"
  }
}



