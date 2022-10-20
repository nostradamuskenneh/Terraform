# # create application load balancer
# aws_region = "us-east-1"

# alb_name                   = "jenkins"
# internal                   = false
# load_balancer_type         = "application"
# alb-subnets                = ["subnet-0890d120f106adcd3", "subnet-0d24d4e142aac0b29"]
# alb_security_groups        = ["sg-076ae3417d38ffe3c"]
# vpc_id                     = "vpc-0c5aaf2965a673d06"
# certificate_arn            = "arn:aws:acm:us-east-1:788210522308:certificate/3c0a5987-3dfb-44d8-a1cb-8f3a0a0c2bb3"
# enable_deletion_protection = false


# # create target group
# name_prefix          = "app1-"
# target_type          = "instance"
# port                 = "80"
# protocol             = "HTTP"
# deregistration_delay = 10

# health_check = {
#   enabled             = true
#   interval            = 30
#   port                = "traffic-port"
#   path                = "/app1/index.html"
#   timeout             = 60
#   matcher             = 200
#   healthy_threshold   = 5
#   unhealthy_threshold = 5
# }

# # common tags
# common_tags = {
#   "AssetID"       = "2560"
#   "AssetName"     = "Insfrastructure"
#   "AssetAreaName" = "ADL"
#   "ControlledBy"  = "Terraform"
#   "cloudProvider" = "aws"
#   "Name"          = "jenkins-alb"
# }

