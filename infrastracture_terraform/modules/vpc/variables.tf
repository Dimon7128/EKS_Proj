variable "cidr_block" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "cidr_block_private_A" {
  description = "CIDR block for the private subnet in AZ A"
  type        = string
}

variable "cidr_block_public_A" {
  description = "CIDR block for the public subnet in AZ A"
  type        = string
}

variable "cidr_block_private_B" {
  description = "CIDR block for the private subnet in AZ B"
  type        = string
}

variable "cidr_block_public_B" {
  description = "CIDR block for the public subnet in AZ B"
  type        = string
}

variable "AZ_A" {
  description = "Availability Zone A"
  type        = string
}

variable "AZ_B" {
  description = "Availability Zone B"
  type        = string
}







# Define other variables like subnet CIDR blocks here









