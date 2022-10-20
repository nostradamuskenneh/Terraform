region              = "us-east-1"
dynamodb-table-name = "ektec-terraform-state-lock"
read_capacity       = 5
write_capacity      = 5

bucket-name       = "ektec-terraform-state"
versioning_enable = true

tags = {
  Owner       = "PECS"
  Project     = "alpha"
  Environment = "development"
  Create_By   = "Terraform"
}
