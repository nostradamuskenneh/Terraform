terraform {
  source = "../../../terraform/modules/vpc/vpc1"
}

include {
  path = find_in_parent_folders()
}

inputs = {
    region             = "us-east-1"
    availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
    cidr_block         = "10.0.0.0/16"
    vpc_name           = "alpha"

    tags = {
      Owner       = "PECS"
      Project     = "alpha"
      Environment = "production"
      Create_By   = "Terraform"
    }
}



