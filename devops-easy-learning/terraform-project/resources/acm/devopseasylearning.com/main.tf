module "acm" {
  source                    = "../../../modules/acm"
  aws_region                = var.aws_region
  domain_name               = var.domain_name
  subject_alternative_names = var.subject_alternative_names
  common_tags               = var.common_tags
}
