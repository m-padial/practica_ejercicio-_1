# Repositorio ECR
resource "aws_ecr_repository" "api_repository" {
  name = "intento_terraform"
}

# Rol IAM para acceso a ECR desde App Runner
resource "aws_iam_role" "apprunner_role" {
  name = "apprunner-ecr-access-role"
  
  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "build.apprunner.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  })
}

# Adjuntar política de acceso a ECR específica para App Runner
resource "aws_iam_role_policy_attachment" "apprunner_policy_attachment" {
  role       = aws_iam_role.apprunner_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSAppRunnerServicePolicyForECRAccess"
}

# Servicio App Runner
resource "aws_apprunner_service" "dash_app" {
  service_name = "skew-volatilidad-app"

  source_configuration {
    authentication_configuration {
      access_role_arn = aws_iam_role.apprunner_role.arn
    }

    image_repository {
      image_configuration {
        port = "8050"
      }
      image_identifier      = "${aws_ecr_repository.api_repository.repository_url}:latest"
      image_repository_type = "ECR"
    }

    auto_deployments_enabled = false
  }

  tags = {
    Name = "skew-volatilidad-app"
  }
}
