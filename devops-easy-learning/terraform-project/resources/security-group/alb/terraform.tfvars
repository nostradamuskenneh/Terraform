aws_region     = "us-east-1"
vpc_id         = "vpc-0c5aaf2965a673d06"
sg_protocol    = "tcp"
sg_name        = "alb-security-group"
sg_desc        = "This security group allows traffic on ports 80, 443"
ports_in       = ["80", "443"]
cidrs_in       = ["0.0.0.0/0"]
cidrs_out      = ["0.0.0.0/0"]
include_egress = "0"
inbound_ping   = false

common_tags = {
  "AssetID"       = "2560"
  "AssetName"     = "Insfrastructure"
  "AssetAreaName" = "ADL"
  "ControlledBy"  = "Terraform"
  "cloudProvider" = "aws"
  "Name"          = "alb-security-group"
}

