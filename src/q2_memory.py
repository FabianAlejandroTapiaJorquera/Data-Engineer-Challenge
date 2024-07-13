from typing import List, Tuple
from memory_profiler import profile
import jsonlines
from collections import Counter
import regex as re

# regex de emojis más comunes
emoji_pattern = re.compile(
    r'[\p{Emoji_Presentation}\p{Extended_Pictographic}]'
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