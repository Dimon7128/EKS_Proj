output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "public_subnets" {
  description = "IDs of the public subnets"
  value = [
    aws_subnet.public_A.id,
    aws_subnet.public_B.id, 
    # Add other public subnets as needed
  ]
}

output "private_subnets" {
  description = "IDs of the private subnets"
  value = [
    aws_subnet.private_A.id,
    aws_subnet.private_B.id,
    # Add other private subnets as needed
  ]
  }

output "internet_gateway_id" {
  description = "The ID of the Internet Gateway"
  value       = aws_internet_gateway.igw.id
}

output "nat_gateway_id" {
  description = "The ID of the NAT Gateway"
  value       = aws_nat_gateway.nat_gateway.id
}

