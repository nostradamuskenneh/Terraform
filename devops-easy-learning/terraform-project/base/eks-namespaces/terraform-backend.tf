terraform {
  backend "s3" {
    bucket         = "ektec-terraform-state"
    key            = "aws-terraform/namespaces/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ektec-terraform-state-lock"
  }
}
