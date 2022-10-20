## bastion public
output "bastion_public" {
  description = "List of IDs of instances"
  value       = aws_instance.bamboo.public_ip
}
