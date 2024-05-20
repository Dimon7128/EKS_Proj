terraform {
  backend "s3" {
    bucket         = "terrafomstatefile"
    key            = "terraform.tfstate"
    region         = "eu-west-3"
    #dynamodb_table = "my-terraform-state-lock"
    encrypt        = true
  }
}


provider "aws" {
  region = var.aws_region
}


module "vpc" {
  source               = "./modules/vpc"
  cidr_block           = var.cidr_block
  cidr_block_private_A = var.cidr_block_private_A
  cidr_block_public_A  = var.cidr_block_public_A
  cidr_block_private_B = var.cidr_block_private_B
  cidr_block_public_B  = var.cidr_block_public_B
  AZ_A                 = var.AZ_A
  AZ_B                 = var.AZ_B
  // Pass any other required variables
}

provider "kubernetes" {
  host                   = module.eks-cluster.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks-cluster.cluster_certificate_authority_data)
  token                  = data.aws_eks_cluster_auth.cluster.token
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks-cluster.cluster_id
}



module "eks-cluster" {
  source = "./modules/eks-cluster"

  cluster_name    = var.cluster_name
  cluster_version = var.cluster_version
  vpc_id          = module.vpc.vpc_id
  private_subnets = module.vpc.private_subnets
  public_subnets  = module.vpc.public_subnets
  cluster_role_arn = var.cluster_role_arn 
  desired_capacity = var.desired_capacity
  max_capacity     = var.max_capacity
  min_capacity     = var.min_capacity
  instance_types   = var.instance_types
}

 