terraform {
  backend "s3" {
    bucket         = "ektec-terraform-student-state"
    key            = "dev/module-ec2/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ektec-terraform-student-state-lock"
  }
}

