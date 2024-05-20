variable "cluster_name" {
  description = "Best cluster"
  type        = string
}

variable "cluster_version" {
  description = "The desired Kubernetes version for the EKS cluster"
  type        = string
}

variable "vpc_id" {
  description = "The VPC ID where the EKS cluster will be deployed"
  type        = string
}

variable "private_subnets" {
  description = "A list of private subnet IDs to deploy the EKS cluster"
  type        = list(string)
}

variable "public_subnets" {
  description = "A list of public subnet IDs for the EKS worker nodes"
  type        = list(string)
}

variable "cluster_role_arn" {
  description = "ARN of the AWS IAM role that provides permissions for the EKS cluster."
  type        = string
}

variable "desired_capacity" {
  description = "Desired number of worker nodes"
  type        = number
}

variable "max_capacity" {
  description = "Maximum number of worker nodes"
  type        = number
}

variable "min_capacity" {
  description = "Minimum number of worker nodes"
  type        = number
}
variable "instance_types" {
  description = "List of instance types for the EKS Node Group."
  type        = list(string)
}

// Include other variables as needed

