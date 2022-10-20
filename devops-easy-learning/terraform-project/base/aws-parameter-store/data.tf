data "aws_ssm_parameter" "db-password" {
  name = "${var.param_store_prefix}/db-password"
}

data "aws_ssm_parameter" "db-username" {
  name = "${var.param_store_prefix}/db-username"
}


# data.aws_ssm_parameter.db-password.value
# data.aws_ssm_parameter.db-username.value

output "db-password" {
  sensitive = true
  value     = data.aws_ssm_parameter.db-password.value
}

output "db-username" {
  sensitive = true
  value     = data.aws_ssm_parameter.db-username.value
}


/*
RESULT:
Outputs:
db-password = <sensitive>
db-username = <sensitive>
*/

/*
// CREATE A DATABASE WITH USERNAME AND PASSWORD
password = data.aws_ssm_parameter.db-password.value
username = data.aws_ssm_parameter.db-username.value
*/
