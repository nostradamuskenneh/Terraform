variable "param_store_prefix" {
  type    = string
  default = "/2560/adl"
}

variable "common_tags" {
  type = map(any)
  default = {
    "AssetID"       = "2560"
    "AssetName"     = "Insfrastructure"
    "AssetAreaName" = "ADL"
    "ControlledBy"  = "Terraform"
    "cloudProvider" = "aws"
  }
}
