module "terraform-backend" {
  source            = "../../../modules/terraform-backend"
  aws_region        = var.aws_region
  enable_versioning = var.enable_versioning
  read_capacity     = var.read_capacity
  write_capacity    = var.write_capacity
  common_tags       = var.common_tags
}


