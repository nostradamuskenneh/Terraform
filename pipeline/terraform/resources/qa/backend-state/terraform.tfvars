region              = "us-east-1"
dynamodb-table-name = "ektec-qa-terraform-state-lock"
read_capacity       = 5
write_capacity      = 5

bucket-name       = "ektec-qa-terraform-state"
versioning_enable = true

tags = {
  Owner       = "PECS"
  Project     = "alpha"
  Environment = "qa"
  Create_By   = "Terraform"
}
