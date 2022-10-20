# https://github.com/terraform-aws-modules/terraform-aws-rds/blob/master/examples/complete-mysql/main.tf

resource "aws_db_instance" "bamboo-db-mysql" {
  instance_class          = "db.t2.small" #1cpu and 2G of ram
  identifier              = "bamboo"
  engine                  = "mysql"
  engine_version          = "5.7"
  multi_az                = false
  deletion_protection     = false
  storage_type            = "gp2"
  port                    = 3306
  allocated_storage       = 20
  max_allocated_storage   = 50
  name                    = "bamboo" # This will create a db call bamboo
  username                = "admin"
  password                = data.aws_ssm_parameter.bamboo-db-password.value
  apply_immediately       = "true"
  backup_retention_period = 0
  skip_final_snapshot     = true
  # backup_window           = "09:46-10:16"
  db_subnet_group_name   = aws_db_subnet_group.bamboo-mysql-db-subnet.name
  vpc_security_group_ids = ["${aws_security_group.bamboo-mysql-db-sg.id}"]
}

resource "aws_db_subnet_group" "bamboo-mysql-db-subnet" {
  name = "bamboo-mysql-db-subnet"
  subnet_ids = [
    "${data.aws_subnet.db-subnet-public-01.id}",
    "${data.aws_subnet.db-subnet-public-02.id}",
  ]
}

resource "aws_security_group" "bamboo-mysql-db-sg" {
  name   = "mysql-rds-sg"
  vpc_id = data.aws_vpc.bamboo_vpc.id
}

resource "aws_security_group_rule" "mysql-rds-sg-rule" {
  from_port         = 3306
  protocol          = "tcp"
  security_group_id = aws_security_group.bamboo-mysql-db-sg.id
  to_port           = 3306
  type              = "ingress"
  cidr_blocks       = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "outbound_rule" {
  from_port         = 0
  protocol          = "-1"
  security_group_id = aws_security_group.bamboo-mysql-db-sg.id
  to_port           = 0
  type              = "egress"
  cidr_blocks       = ["0.0.0.0/0"]
}
