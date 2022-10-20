aws_region        = "us-east-1"
enable_versioning = true
common_tags = {
  "AssetID"       = "2560"
  "AssetName"     = "Insfrastructure"
  "Environment"   = "prod"
  "Project"       = "alpha"
  "CreateBy"      = "Terraform"
  "cloudProvider" = "aws"
}

read_capacity  = 5
write_capacity = 5
