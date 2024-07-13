from typing import List, Tuple
from memory_profiler import profile
import jsonlines
from collections import Counter
import regex as re

# regex de emojis más comunes
emoji_pattern = re.compile(
    r'[\U0001F600-\U0001F64F]'  # Emoticons
    r'|[\U0001F300-\U0001F5FF]'  # Símbolos y pictogramas
    r'|[\U0001F680-\U0001F6FF]'  # Transporte y símbolos
    r'|[\U0001F700-\U0001F77F]'  # Alquimia
    r'|[\U0001F780-\U0001F7FF]'  # Geométricos
    r'|[\U0001F800-\U0001F8FF]'  # Suplemento de flechas
    r'|[\U0001F900-\U0001F9FF]'  # Suplemento de pictogramas
    r'|[\U0001FA00-\U0001FA6F]'  # Suplemento adicional de pictogramas
    r'|[\U0001FA70-\U0001FAFF]'  # Suplemento adicional de pictogramas 2'
    r'|[\U00002702-\U000027B0]'  # Diversos símbolos (✂️, ✈️)
    r'|[\U000024C2-\U0001F251]'  # Letras enmarcadas y símbolos variados
    r'|[\U0001F004]'  # Mahjong Tile Red Dragon
    r'|[\U0001F0CF]'  # Playing Card Black Joker
)

# @profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # variables para contar los emojis
    contadorEmojis = Counter()
    totalEmojis = 0
    # variable donde almacenaremos nuestros resultados
    resultado: List[Tuple[str, int]] = []
    # abrimos el archivo json
    with jsonlines.open(file_path) as twitter:
        # recorrimos cada publicación dentro del archivo
        for publicacion in twitter:
            # publicaciones se encuentran en 'content'
            contenido = publicacion['content']
            if contenido:
                # filtramos los emojis de la publicación con ayuda de la expresión regular
                emojisEncontrados = emoji_pattern.findall(contenido)
                contadorEmojis.update(emojisEncontrados)
                totalEmojis += len(emojisEncontrados)
    # almacenamiento de los resultados
    for emoji, count in contadorEmojis.most_common(10):
        resultado.append((emoji, count))
    return resultado