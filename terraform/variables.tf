variable "region" {
  description = "Región de AWS"
  type        = string
  default     = "eu-west-1"
}

variable "ecr_repo_name" {
  description = "Nombre del repositorio ECR"
  type        = string
  default     = "intento_terraform"
}

variable "app_runner_service_name" {
  description = "Nombre del servicio App Runner"
  type        = string
  default     = "skew-volatilidad-app"
}

variable "image_tag" {
  description = "Etiqueta de la imagen Docker"
  type        = string
  default     = "latest"
}

variable "dynamodb_table_name" {
  description = "Nombre de la tabla DynamoDB"
  type        = string
  default     = "OpcionesVolatilidad"
}
