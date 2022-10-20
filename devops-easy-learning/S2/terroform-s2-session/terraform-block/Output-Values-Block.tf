
output "foo" {
  value = data.aws_vpc.foo.id
}

output "foo2" {
  value = data.aws_vpc.foo2.id
}

output "EC2_web" {
  value = aws_instance.app_server.id
}
