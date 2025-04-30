output "app_runner_url" {
  description = "URL pública de App Runner"
  value       = aws_apprunner_service.dash_app.service_url
}

output "ecr_repo_url" {
  description = "URL del repositorio ECR"
  value       = aws_ecr_repository.dash_repo.repository_url
}

