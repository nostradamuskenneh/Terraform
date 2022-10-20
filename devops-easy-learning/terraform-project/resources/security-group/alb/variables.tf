variable "vpc_id" {
  type = string
}

variable "sg_protocol" {
  type    = string
  default = "tcp"
}

variable "common_tags" {
  type = map(string)
}

variable "sg_name" {
  type    = string
  default = "test-security-group"
}

variable "sg_desc" {
  type    = string
  default = "Secure Web Access Only"
}

variable "ports_in" {
  type        = list(string)
  description = "list of ports"
  default     = [443, 80]
}

variable "ports_out" {
  type        = list(string)
  description = "list of ports"
  default     = ["0.0.0.0/0"]
}

variable "aws_region" {
  type        = string
  description = "Region for SG"
  default     = "us-east-1"
}

variable "cidrs_in" {
  type        = list(string)
  default     = ["10.179.154.208/32", "10.179.154.108/32"]
  description = "Default list of cidrs"
}

variable "cidrs_out" {
  type        = list(string)
  default     = ["10.179.154.208/32", "10.179.154.108/32"]
  description = "Default list of cidrs"
}

variable "include_egress" {
  type        = string
  default     = "0"
  description = " "
}

variable "inbound_ping" {
  type        = bool
  default     = false
  description = " "
}
