from typing import List, Tuple
import json
from collections import Counter
import regex as re
from time_profile import profile_with_timing

# Regex para detectar menciones de usuarios
mencionRegex = re.compile(r'@(\w+)')

# @profile_with_timing(sortby='time')
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # contador para las menciones de usuarios
    contadorMenciones = Counter()
    # variable donde almacenaremos nuestros resultados
    resultado: List[Tuple[str, int]] = []
    # Abrimos el archivo JSON
    with open(file_path, 'r', encoding='utf-8') as twitter:
        # Recorremos cada publicación dentro del archivo
        for publicacion in twitter:
            # Publicaciones se encuentran en 'content'
            tweet = json.loads(publicacion)
            contenido = tweet.get('content')
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