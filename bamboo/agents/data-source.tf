data "aws_vpc" "bamboo_vpc" {
  filter {
    name   = "tag:Name"
    values = ["Tia-public"]
  }
}

data "aws_subnet" "db-subnet-public-01" {
  filter {
    name   = "tag:Name"
    values = ["public-subnet-01"]
  }
}

data "aws_subnet" "db-subnet-public-02" {
  filter {
    name   = "tag:Name"
    values = ["public-subnet-02"]
  }
}

