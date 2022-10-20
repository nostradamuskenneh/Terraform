# Get secret information for RDS password
data "aws_secretsmanager_secret" "rds_password" {
  name = "2568/adl/db/databases-password"
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
  name = "2568/adl/db/databases-username"
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
password = data.aws_secretsmanager_secret_version.rds_password.secret_string
username = data.aws_secretsmanager_secret_version.rds_username.secret_string
*/
