terraform {
  backend "s3" {
    bucket = "tia-terraform-state-backend"
    key    = "terraform-backend-state/vpc/mam-dev"
    region = "us-east-1"
    # dynamodb_table = "terraform_state"
  }
}
