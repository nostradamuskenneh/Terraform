resource "aws_s3_bucket" "bucket" {
  bucket = format("%s-%s-%s-terraform-state", var.common_tags["AssetID"], var.common_tags["Environment"], var.common_tags["Project"])
  versioning {
    enabled = var.enable_versioning
  }
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
  object_lock_configuration {
    object_lock_enabled = "Enabled"
  }
  tags = var.common_tags
}

resource "aws_dynamodb_table" "terraform-lock" {
  name           = format("%s-%s-%s-terraform-state-lock", var.common_tags["AssetID"], var.common_tags["Environment"], var.common_tags["Project"])
  read_capacity  = var.read_capacity
  write_capacity = var.write_capacity
  hash_key       = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
  tags = var.common_tags
}





