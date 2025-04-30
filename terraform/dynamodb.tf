resource "aws_dynamodb_table" "opciones_volatilidad" {
  name         = "OpcionesVolatilidad"
  billing_mode = "PAYPERREQUEST"
  hash_key     = "fecha_scraping"
  range_key    = "strike"

  attribute {
    name = "fecha_scraping"
    type = "S"
  }

  attribute {
    name = "strike"
    type = "S"
  }

  tags = {
    Name     = "OpcionesVolatilidad"
    Proyecto = "Volatilidad IBEX"
  }
}
