import os
import re

# Directorio de ejecución del script
directorio = os.getcwd()

# Patrones de búsqueda y reemplazo
patrones = [
    (r"{{ url_for\('static', filename='", r"{% static '"),
    (r"'\) }}", r"' %}"),
    (r"{{ url_for\('static', filename='", r"{% static '"),
    (r"'\) }}", r"' %}")
]

# Función para procesar cada archivo
def procesar_archivo(archivo):
    # Lee el contenido del archivo
    with open(archivo, 'r') as f:
        contenido = f.read()

    # Aplica los patrones de búsqueda y reemplazo
    for patron, reemplazo in patrones:
        contenido = re.sub(patron, reemplazo, contenido)

    # Escribe el contenido modificado de vuelta al archivo
    with open(archivo, 'w') as f:
        f.write(contenido)

# Itera sobre los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".html"):
        archivo_path = os.path.join(directorio, archivo)
        procesar_archivo(archivo_path)

print("Proceso completado.")
