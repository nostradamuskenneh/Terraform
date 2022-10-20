# terraform {
#   backend "s3" {
#     bucket         = "ektec-terraform-state"
#     key            = "aws-terraform/ec2/ec2-private/terraform.tfstate"
#     region         = "us-east-1"
#     dynamodb_table = "ektec-terraform-state-lock"
#   }
# }
