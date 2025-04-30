import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
tabla = dynamodb.Table("OpcionesVolatilidad")

def guardar_en_dynamodb(df):
    fecha = datetime.today().strftime("%Y-%m-%d")

    for _, row in df.iterrows():
        item = {
            "fecha_scraping": fecha,
            "strike": str(row['strike']),  
            "put_call": row.get("put/call", ""),
            "precio_ant": float(row.get("ant", 0)),
            "volatilidad": float(row.get("σ", 0)),
            "vencimiento": str(row.get("FV", "N/A")),
        }

        tabla.put_item(Item=item)
