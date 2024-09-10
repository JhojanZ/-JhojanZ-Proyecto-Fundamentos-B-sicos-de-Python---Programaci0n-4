import pandas as pd
from tabulate import tabulate

def crear_tabla(datos_suelo):
    pd.set_option('display.max_columns', None)

    # Variables edáficas y sus nuevos nombres
    variables_edaficas = ["ph_agua_suelo_2_5_1_0", "f_sforo_p_bray_ii_mg_kg", "potasio_k_intercambiable_cmol_kg"]
    nuevos_nombres = {
        "ph_agua_suelo_2_5_1_0": "PH en Agua",
        "f_sforo_p_bray_ii_mg_kg": "Fósforo (mg/kg)",
        "potasio_k_intercambiable_cmol_kg": "Potasio (cmol/kg)"
    }

    columnas = ["departamento", "municipio", "cultivo", "topografia"] + variables_edaficas
    tabla_resultados = datos_suelo[columnas].copy()
    
    tabla_resultados = tabla_resultados.rename(columns=nuevos_nombres)
    return tabla_resultados

def imprimir_medianas(datos_suelo):
    variables_edaficas = ["ph_agua_suelo_2_5_1_0", "f_sforo_p_bray_ii_mg_kg", "potasio_k_intercambiable_cmol_kg"]
    nuevos_nombres = {
        "ph_agua_suelo_2_5_1_0": "PH en Agua",
        "f_sforo_p_bray_ii_mg_kg": "Fósforo (mg/kg)",
        "potasio_k_intercambiable_cmol_kg": "Potasio (cmol/kg)"
    }

    for var in variables_edaficas:
        datos_suelo[var] = pd.to_numeric(datos_suelo[var], errors='coerce')

    medianas = datos_suelo[variables_edaficas].median()

    print("Medianas de las variables edáficas:")
    for variable in variables_edaficas:
        nombre = nuevos_nombres.get(variable, variable)
        print(f"{nombre}: {medianas[variable]:.2f}")

def mostrar_datos(datos):
    # Convertir el DataFrame a una lista de listas
    headers = datos.columns.tolist()
    rows = datos.values.tolist()

    print(tabulate(rows, headers=headers, tablefmt="grid"))

