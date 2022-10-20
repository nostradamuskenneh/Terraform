# terraform {
#   backend "s3" {
#     bucket         = "ektec-development-terraform-state"
#     key            = "terraform-backend-vpc-state/vpc-test"
#     region         = "us-east-1"
#     dynamodb_table = "ektec-development-terraform-state-lock"
#   }
# }
