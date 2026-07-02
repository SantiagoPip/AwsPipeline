import pandas as pd
from src.transform import limpiar_transacciones

# 1. Crear datos de prueba simulando el CSV
datos_ficticios = {
    "transaction_id": [101, 102, 103],
    "amount": [50.5, None, 120.0]  # El 102 tiene un nulo, debería eliminarse
}
df_test = pd.DataFrame(datos_ficticios)

print("--- DATOS ORIGINALES ---")
print(df_test)

# 2. Llamar a tu función de la carpeta src
df_resultado = limpiar_transacciones(df_test)

print("\n--- DATOS LIMPIOS ---")
print(df_resultado)