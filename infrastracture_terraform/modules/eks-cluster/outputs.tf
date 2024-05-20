output "cluster_id" {
  description = "The EKS cluster ID"
  value       = module.eks.cluster_id
}

output "cluster_name" {
  description = "Yossi_Baliti"
  value       = module.eks.cluster_id

}
output "cluster_arn" {
  description = "The EKS cluster ARN"
  value       = module.eks.cluster_arn
}

output "cluster_certificate_authority_data"{
  description = "The EKS cluster ARN"
  value       = module.eks.cluster_certificate_authority_data

}

output "cluster_endpoint" {
  description = "The endpoint for your EKS Kubernetes API"
  value       = module.eks.cluster_endpoint
}

output "cluster_security_group_id" {
  description = "The security group ID attached to the EKS cluster"
  value       = module.eks.cluster_security_group_id
}


// Include other outputs as needed

