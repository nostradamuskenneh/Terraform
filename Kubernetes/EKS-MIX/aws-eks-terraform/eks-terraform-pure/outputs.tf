output "aws_ecr_name" {
  value = aws_ecr_repository.container_repository.name
}

output "aws_ecr_id" {
  value = aws_ecr_repository.container_repository.registry_id
}

output "aws_ecr_tags" {
  value = var.common_tags
}

output "aws_ecr_url" {
  value = aws_ecr_repository.container_repository.repository_url
}



