module "acm" {
  source         = "../../../modules/security-group"
  aws_region     = var.aws_region
  vpc_id         = var.vpc_id
  sg_protocol    = var.sg_protocol
  sg_name        = var.sg_name
  sg_desc        = var.sg_desc
  ports_in       = var.ports_in
  ports_out      = var.ports_out
  cidrs_in       = var.cidrs_in
  cidrs_out      = var.cidrs_out
  include_egress = var.include_egress
  inbound_ping   = var.inbound_ping
  common_tags    = var.common_tags
}



