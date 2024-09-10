import pandas as pd
from sodapy import Socrata

def obtener_datos_suelo(datos):
    departamento, municipio, cultivo, numero_registros = datos
    client = Socrata("www.datos.gov.co", None)

    query = f"departamento='{departamento}' AND municipio='{municipio}' AND cultivo='{cultivo}'"

    resultados = client.get("ch4u-f3i5", where=query, limit=int(numero_registros))
    if not resultados:
        print("No se encontraron resultados.")
        return None
    
    return pd.DataFrame.from_records(resultados)
