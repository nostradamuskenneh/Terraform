terraform {
  backend "s3" {
    bucket         = "ektec-terraform-student-state"
    key            = "dev/terraform-blocks/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ektec-terraform-student-state-lock"
  }
}

