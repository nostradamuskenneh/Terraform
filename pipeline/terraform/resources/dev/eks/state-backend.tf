terraform {
  backend "s3" {
    bucket = "tia-terraform-state-backend"
    key    = "terraform-backend-state/eks-control-plane"
    region = "us-east-1"
    # dynamodb_table = "terraform_state"
  }
}
