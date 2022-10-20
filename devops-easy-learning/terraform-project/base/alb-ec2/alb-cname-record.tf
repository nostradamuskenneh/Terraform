resource "aws_route53_record" "cluster-alias" {
  depends_on = [module.alb]
  zone_id    = "Z09063052B43KCQ7FSGHY"
  name       = "web"
  type       = "CNAME"
  ttl        = "60"
  records    = [module.alb.lb_dns_name]
}
