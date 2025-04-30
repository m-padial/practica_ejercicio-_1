variable "region" {
  description = "Región de AWS"
  type        = string
  default     = "eu-west-1"
}

variable "ecr_repo_name" {
  description = "Nombre del repositorio ECR"
  type        = string
  default     = "miax_13_practica"
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
