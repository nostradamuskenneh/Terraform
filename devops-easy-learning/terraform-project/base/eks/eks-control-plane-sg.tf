## The EKS security will be created automatically when the control plane is created
## We can always create a custom sg if we do not want the default one

resource "aws_security_group" "control-plane-sg" {
  name        = "${var.control_plane_name}-control-plane-sg"
  description = "Cluster communication with worker nodes"
  vpc_id      = data.aws_vpc.adl_eks_vpc.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "${var.control_plane_name} EKS Cluster communication with worker nodes"
  }
}
