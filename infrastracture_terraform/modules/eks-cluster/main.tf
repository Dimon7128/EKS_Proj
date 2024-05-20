module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  version = "17.24.0"
  cluster_name    = var.cluster_name
  cluster_version = var.cluster_version
  vpc_id          = var.vpc_id
  subnets         = var.public_subnets
 

  node_groups = {
    ng1 = {
      desired_capacity = var.desired_capacity
      max_capacity     = var.max_capacity
      min_capacity     = var.min_capacity
      instance_types   = var.instance_types
      subnets          = var.private_subnets
    }
  }

  # Add additional configurations here
}

