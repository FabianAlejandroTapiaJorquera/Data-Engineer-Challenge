from typing import List, Tuple
from datetime import datetime
import pandas as pd
import jsonlines
from time_profile import profile_with_timing

# Función para obtener el usuario con más publicaciones en cada fecha
def obtenerUsuario(df, fecha):
    dfFecha = df[df['fecha'] == fecha]
    contadorUsuarios = dfFecha['usuarios'].value_counts()
    usuarioTop = contadorUsuarios.idxmax()
    return usuarioTop

# @profile_with_timing(sortby='time')
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # variable donde almacenaremos nuestros resultados
    resultado: List[Tuple[datetime.date, str]] = []
    # Listas para almacenar los datos extraídos
    fechas = []
    usuarios = []
    # Lectura del archivo JSON línea por línea y extracción de datos
    with jsonlines.open(file_path) as twitter:
        for publicacion in twitter:
            fecha = publicacion['date']
            idUsuario= publicacion['user']['id']
            fechas.append(fecha)
            usuarios.append(idUsuario)       
    # Crear un DataFrame con los datos extraídos
    df = pd.DataFrame({'fecha': fechas, 'usuarios': usuarios})
    # Extraer solo la fecha del campo 'date'
    df['fecha'] = pd.to_datetime(df['fecha']).dt.date
    # Contar el número de publicaciones por día
    publicacionesDiarias = df['fecha'].value_counts().head(10)
    # Almacenar los resultados
    for item in publicacionesDiarias.index:
        usuarioTop = obtenerUsuario(df, item)
        resultado.append((item, str(usuarioTop)))
    return resultado