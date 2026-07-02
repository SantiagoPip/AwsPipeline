import os
import boto3
import pandas as pd
from src.transform import limpiar_transacciones

# Inicializamos el cliente de AWS S3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # 1. Obtener los nombres de los buckets de forma dinámica (los enviaremos desde el orquestador)
        bucket_origen = event.get('BUCKET_ORIGEN', 'tu-bucket-bronze-por-defecto')
        bucket_destino = event.get('BUCKET_DESTINO', 'tu-bucket-silver-por-defecto')
        
        nombre_archivo = "transacciones.csv"
        
        # 2. Descargar el archivo desde S3 Bronze directamente a la memoria de la Lambda
        print(f"Leyendo {nombre_archivo} desde el bucket {bucket_origen}...")
        obj = s3_client.get_object(Bucket=bucket_origen, Key=nombre_archivo)
        
        # 3. Cargar el contenido en un DataFrame de Pandas
        df_raw = pd.read_csv(obj['Body'])
        
        # 4. Usar TU función modular que ya probaste en local
        df_limpio = limpiar_transacciones(df_raw)
        
        # 5. Convertir el resultado limpio a formato CSV (o Parquet) en texto/bytes
        csv_buffer = df_limpio.to_csv(index=False)
        
        # 6. Subir el archivo limpio a la capa Silver de S3
        ruta_salida = "transacciones_limpias.csv"
        print(f"Subiendo archivo limpio a {bucket_destino}/{ruta_salida}...")
        
        s3_client.put_object(
            Bucket=bucket_destino,
            Key=ruta_salida,
            Body=csv_buffer
        )
        
        return {
            'statusCode': 200,
            'body': '¡Pipeline de Python puro ejecutado con éxito en AWS Lambda!'
        }
        
    except Exception as e:
        print(f"Error en el pipeline: {str(e)}")
        raise e