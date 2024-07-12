from typing import List, Tuple
from datetime import datetime
from memory_profiler import profile
import jsonlines
from collections import defaultdict
from typing import List, Tuple

# variable donde almacenaremos nuestros resultados
resultado: List[Tuple[datetime.date, str]] = []
# diccionario para contar las publicaciones por fecha y las publicaciones por usuario por fecha
contadorFechas = defaultdict(int)
contadorUsuarioFecha = defaultdict(lambda: defaultdict(int))

# función auxiliar para obtener el usuario con más publicaciones en cada fecha
def obtenerUsuario(fecha):
    contadorUsuarios = contadorUsuarioFecha[fecha]
    mayorUsuario = max(contadorUsuarios, key=contadorUsuarios.get)
    return mayorUsuario

# @profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # procesamiento de cada elemento dentro del archivo json
    with jsonlines.open(file_path) as twitter:
        for publicacion in twitter:
            # fecha y usaurio actual
            fecha = publicacion['date']
            usuario = publicacion['user']['id']
            # borrado del objeto para liberar memoria
            del publicacion
            # condicionales
            # contadores de cuantas veces se repite cada elemento
            if fecha:
                contadorFechas[fecha] += 1
                if usuario:
                    contadorUsuarioFecha[fecha][usuario] += 1
    # ordenamiento de las 10 fechas con más publicaciones
    top10Fechas= sorted(contadorFechas.items(), key=lambda x: x[1], reverse=True)[:10]
    # almacenamiento de los resultados
    for fecha, count in top10Fechas:
        usuarioTop = obtenerUsuario(fecha) 
        resultado.append((fecha, usuarioTop))
    return resultado
