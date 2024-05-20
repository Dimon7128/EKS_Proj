variable "aws_region" {
  description = "AWS region"
}

variable "cidr_block" {
  description = "CIDR block for the VPC"
}


variable "cidr_block_private_A" {
  description = "CIDR block for the first private subnet."
}

variable "cidr_block_public_A" {
  description = "CIDR block for the first public subnet."
}

variable "cidr_block_private_B" {
  description = "CIDR block for the second private subnet."
}

variable "cidr_block_public_B" {
  description = "CIDR block for the second public subnet."
}

variable "AZ_A" {
  description = "Availability Zone A."
}

variable "AZ_B" {
  description = "Availability Zone B."
}

variable "cluster_name" {
  description = "name_of_the_cluster"
}

variable "cluster_role_arn" {
  description = "arn_of_the_cluster"
}
variable "cluster_version" {
  description = "Yossi_Baliti"
}
variable "desired_capacity" {
  description = "The desired number of instances in the EKS Node Group."
}

variable "max_capacity" {
  description = "The maximum number of instances in the EKS Node Group."
}

variable "min_capacity" {
  description = "The minimum number of instances in the EKS Node Group."
}

variable "instance_types" {
  description = "List of instance types for the EKS Node Group."
  type        = list(string)
}


