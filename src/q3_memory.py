from typing import List, Tuple
import jsonlines
from collections import Counter
import regex as re
from memory_profiler import profile

# Regex para detectar menciones de usuarios
mencionRegex = re.compile(r'@(\w+)')

# @profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # contador para las menciones de usuarios
    contadorMenciones = Counter()
    # variable donde almacenaremos nuestros resultados
    resultado: List[Tuple[str, int]] = []
    # Abrimos el archivo JSON
    with jsonlines.open(file_path) as twitter:
        # Recorremos cada publicación dentro del archivo
        for publicacion in twitter:
            # Publicaciones se encuentran en 'content'
            contenido = publicacion['content']
            if contenido:
                # Filtramos las menciones de usuarios con la expresión regular
                mencionesEncontradas = mencionRegex.findall(contenido)
                contadorMenciones.update(mencionesEncontradas)        
    # Obtener los 10 usuarios más mencionados
    resultadoMenciones = contadorMenciones.most_common(10)
    # almacenamiento de los resultados
    for mencion, count in resultadoMenciones:
        resultado.append((mencion, count))
    return resultado