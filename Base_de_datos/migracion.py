import pandas as pd
import pymysql
import os

# Ruta del archivo CSV
file_path = r"Datasets/peliculasdatos_limpio.csv"

# Verificar si el archivo existe
if not os.path.exists(file_path):
    print(f"El archivo no se encuentra en la ruta: {file_path}")
    exit()

# Cargar el archivo CSV
try:
    data = pd.read_csv(file_path)
    print("Archivo cargado correctamente. Primeras filas:")
    print(data.head())
except Exception as e:
    print("Error al cargar el archivo:", e)
    exit()

# Recortar las duraciones a 10 caracteres
data['duracion'] = data['duracion'].str.slice(0, 10)

# Procesar las duraciones y convertir a minutos
try:
    data['duracion_minutos'] = (
        data['duracion'].str.extract(r'(\d+)h').fillna(0).astype(float) * 60 +
        data['duracion'].str.extract(r'(\d+)m').fillna(0).astype(float)
    )
    print("Duraciones procesadas correctamente.")
except Exception as e:
    print("Error al procesar las duraciones:", e)
    exit()

# Conectar a MySQL
try:
    connection = pymysql.connect(
        host='localhost',  # Cambia esto si tu servidor no está en localhost
        user='root',  # Tu usuario de MySQL
        password='12345678',  # Tu contraseña de MySQL
        database='PeliculasDB',  # Nombre de la base de datos que creaste
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Conexión a la base de datos exitosa.")
except Exception as e:
    print("Error al conectar con la base de datos:", e)
    exit()

# Insertar datos en las tablas
try:
    with connection.cursor() as cursor:
        # Insertar datos en la tabla Anios
        for _, row in data.iterrows():
            cursor.execute("INSERT INTO Anios (ano) VALUES (%s)", (row['ano'],))

        # Obtener los IDs generados para los años
        connection.commit()
        cursor.execute("SELECT * FROM Anios")
        anios_map = {row['ano']: row['id_ano'] for row in cursor.fetchall()}

        # Insertar datos en la tabla Duraciones
        for _, row in data.iterrows():
            cursor.execute(
                "INSERT INTO Duraciones (duracion, duracion_minutos) VALUES (%s, %s)",
                (row['duracion'], row['duracion_minutos'])
            )

        # Obtener los IDs generados para las duraciones
        connection.commit()
        cursor.execute("SELECT * FROM Duraciones")
        duraciones_map = {row['duracion']: row['id_duracion'] for row in cursor.fetchall()}

        # Insertar datos en la tabla Peliculas
        for _, row in data.iterrows():
            id_ano = anios_map.get(row['ano'])
            id_duracion = duraciones_map.get(row['duracion'])

            if id_ano is None:
                print(f"Año no encontrado: {row['ano']}")
                continue

            if id_duracion is None:
                print(f"Duración no encontrada: {row['duracion']}")
                continue

            cursor.execute("""
                INSERT INTO Peliculas (titulo, id_ano, calificacion, id_duracion) 
                VALUES (%s, %s, %s, %s)
            """, (
                row['titulo'],
                id_ano,
                row['calificacion'],
                id_duracion
            ))

        # Confirmar los cambios
        connection.commit()

    print("Datos cargados correctamente en MySQL.")

except Exception as e:
    print("Ocurrió un error durante la carga de datos:", e)

finally:
    connection.close()
    print("Conexión cerrada.")
