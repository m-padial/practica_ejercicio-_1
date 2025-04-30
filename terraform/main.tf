resource "aws_ecr_repository" "dash_repo" {
  name = "intento_terraform"  # Cambiado aquí
}

resource "aws_apprunner_service" "dash_app" {
  service_name = "skew-volatilidad-app"

  source_configuration {
    image_repository {
      image_configuration {
        port = "8050"
      }

      image_identifier      = "${aws_ecr_repository.dash_repo.repository_url}:latest"  # Se actualiza automáticamente
      image_repository_type = "ECR"
    }

    auto_deployments_enabled = true
  }
}
