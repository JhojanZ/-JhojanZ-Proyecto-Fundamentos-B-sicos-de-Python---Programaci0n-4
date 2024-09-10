from api.api import obtener_datos_suelo
from ui.ui import crear_tabla, mostrar_datos, imprimir_medianas

def pedir_datos_usuario():
    departamento = input("Ingrese el Departamento: ").strip().upper()
    municipio = input("Ingrese el Municipio: ").strip().upper()
    cultivo = input("Ingrese el Cultivo: ").strip().lower().capitalize()
    numero_registros = input("Ingrese el número de registros a consultar: ").strip()
    return [departamento, municipio, cultivo, numero_registros]

def main():
    datos = pedir_datos_usuario()    
    datos_suelo = obtener_datos_suelo(datos)
    
    if datos_suelo is not None:
        resultado_tabla = crear_tabla(datos_suelo)
        mostrar_datos(resultado_tabla)
        imprimir_medianas(datos_suelo)
    else:
        print("No se pudieron obtener datos de la API.")

if __name__ == "__main__":
    main()
