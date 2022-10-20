# Provider Block
provider "aws" {
  region = "us-east-2"
}

module "ec2" {
  source = "../../module/ec2"

  instance_name = "prod-instance"
  instance_type = "t2.xlarge"
  instance_key  = "s2-key"
  env           = "production"
  region        = "us-east-2"
}

terraform {
  backend "s3" {
    bucket         = "ektec-terraform-student-state"
    key            = "prod/prod-ec2/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ektec-terraform-student-state-lock"
  }
}

