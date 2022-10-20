# # variable "aws_region" {
# #   type = string
# # }

# variable "common_tags" {
#   type = map(any)
# }

# # create application load balancer
# variable "alb_name" {
#   type = string
# }

# variable "internal" {
#   type    = bool
#   default = false
# }

# variable "load_balancer_type" {
#   type    = string
#   default = "application"
# }

# variable "alb-subnets" {
#   type = list(any)
# }

# variable "alb_security_groups" {
#   type = list(any)
# }

# variable "enable_deletion_protection" {
#   type    = bool
#   default = false
# }

# variable "vpc_id" {
#   type = string
# }

# # create target group
# variable "name_prefix" {
#   type = string
# }

# variable "target_type" {
#   type = string
# }

# variable "port" {
#   type = string
# }

# variable "protocol" {
#   type = string
# }

# variable "deregistration_delay" {
#   type = string
# }

# variable "health_check" {
#   type = map(string)
# }

# # create a listener on port 443 with forward action
# # create a listener on port 80 with redirect action
# variable "certificate_arn" {
#   type = string
# }

