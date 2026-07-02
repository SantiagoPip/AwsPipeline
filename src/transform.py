import pandas as pd

def limpiar_transacciones(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Convertir ID a string
    df['transaction_id'] = df['transaction_id'].astype(str)
    
    # 2. Eliminar filas donde el monto ('amount') sea nulo
    df = df.dropna(subset=['amount'])
    
    # 3. Convertir monto a decimal (float)
    df['amount'] = df['amount'].astype(float)
    
    # 4. Agregar columna con la fecha de procesamiento
    df['fecha_proceso'] = pd.Timestamp.now().strftime('%Y-%m-%d')
    
    return df