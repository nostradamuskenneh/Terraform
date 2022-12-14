resource "aws_db_instance" "postgres-test-sql" {
  instance_class          = "db.t3.micro"
  engine                  = "postgres"
  identifier              = "artifactory"
  engine_version          = "10.20"
  port                    = 5432
  multi_az                = true
  publicly_accessible     = false
  storage_encrypted       = true
  storage_type            = "gp2"
  allocated_storage       = 20
  max_allocated_storage   = 50
  name                    = "pecs"
  username                = "adminuser"
  password                = "Password123"
  apply_immediately       = "true"
  backup_retention_period = 10
  skip_final_snapshot     = true
  backup_window           = "09:46-10:16"
  db_subnet_group_name    = aws_db_subnet_group.postgres-rds-db-subnet.name
  vpc_security_group_ids  = ["${aws_security_group.postgres-rds-sg.id}"]

  tags = {
    Name = "postgres"
  }
}


resource "aws_db_subnet_group" "postgres-rds-db-subnet" {
  name = "postgres-rds-db-subnet"
  subnet_ids = [
    "${data.aws_subnet.eks-db-subnet-01.id}",
    "${data.aws_subnet.eks-db-subnet-02.id}"
  ]
}

resource "aws_security_group" "postgres-rds-sg" {
  name   = "postgres-rds-sg"
  vpc_id = data.aws_vpc.adl_eks_vpc.id
}

resource "aws_security_group_rule" "postgres-rds-sg-rule" {
  from_port         = 5432
  protocol          = "tcp"
  security_group_id = aws_security_group.postgres-rds-sg.id
  to_port           = 5432
  type              = "ingress"
  cidr_blocks       = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "outbound_rule" {
  from_port         = 0
  protocol          = "-1"
  security_group_id = aws_security_group.postgres-rds-sg.id
  to_port           = 0
  type              = "egress"
  cidr_blocks       = ["0.0.0.0/0"]
}
