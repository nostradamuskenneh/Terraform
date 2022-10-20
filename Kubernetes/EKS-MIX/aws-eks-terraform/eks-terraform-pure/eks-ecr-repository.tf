data "aws_caller_identity" "current" {
}

resource "aws_ecr_repository" "container_repository" {
  name = var.ecr_respository_name
  tags = merge(var.common_tags)
}

resource "aws_ecr_lifecycle_policy" "default-ecr-retention-number-policy" {
  repository = aws_ecr_repository.container_repository.name

  policy = <<EOF
{
    "rules": [
        {
            "rulePriority": 1,
            "description": "Expire images greater than ${var.max_number_to_keep}",
            "selection": {
                "tagStatus": "any",
                "countType": "imageCountMoreThan",
                "countNumber": ${var.max_number_to_keep}
            },
            "action": {
                "type": "expire"
            }
        }
    ]
}
EOF
}


variable "ecr_respository_name" {
  type    = string
  default = "develop-repository"
}

variable "max_number_to_keep" {
  type    = string
  default = "5"
}
