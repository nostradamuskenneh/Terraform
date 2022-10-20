
variable "control_plane_name" {
  type    = string
  default = "eks"
}

variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "common_tags" {
  type = map(string)
  default = {
    Environment = "dev"
    Owner       = "pecs-team"
    CreateBy    = "Terraform"
  }
}
