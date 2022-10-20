provider "aws" {
  region = "us-east-1"
}

# Get secret information for RDS password
data "aws_secretsmanager_secret" "rds_password" {
  name = "prod-mam-rds-password"
}

data "aws_secretsmanager_secret_version" "rds_password" {
  secret_id = data.aws_secretsmanager_secret.rds_password.id
}

output "rds_password" {
  sensitive = true
  value     = data.aws_secretsmanager_secret_version.rds_password.secret_string
}


# Get secret information for RDS username
data "aws_secretsmanager_secret" "rds_username" {
  name = "prod-mam-rds-username"
}


data "aws_secretsmanager_secret_version" "rds_username" {
  secret_id = data.aws_secretsmanager_secret.rds_username.id
}

output "rds_username" {
  sensitive = true
  value     = data.aws_secretsmanager_secret_version.rds_username.secret_string
}


/*
RESULT:
Outputs:
rds_password = <sensitive>
rds_username = <sensitive>
*/

/*
// CREATE A DATABASE WITH USERNAME AND PASSWORD
password = data.aws_secretsmanager_secret_version.rds-password.secret_string
username = data.aws_secretsmanager_secret_version.rds-username.secret_string
*/
