from typing import List, Tuple
import jsonlines
from collections import Counter
import regex as re

# Patrón regex para encontrar emojis
emoji_pattern = re.compile(
    r'[\p{Emoji_Presentation}\p{Extended_Pictographic}]'
)

def q2_time(file_path: str) -> List[Tuple[str, int]]:
  # Inicializar contador de emojis
    contadorEmojis = Counter()
    
    # Abrir archivo jsonlines y procesar cada publicación
    with jsonlines.open(file_path) as twitter:
        # Procesar cada línea del archivo jsonlines
        for publicacion in twitter:
            contenido = publicacion['content']
            if contenido:
                # Encontrar emojis en el contenido de la publicación usando regex
                emojis_encontrados = emoji_pattern.findall(contenido)
                # Actualizar el contador de emojis
                contadorEmojis.update(emojis_encontrados)
    # Obtener los 10 emojis más comunes
    resultado = contadorEmojis.most_common(10)
    return resultado