import sqlite3

# Paso 1: Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('escuela.db')

# Paso 2: Crear un cursor
cursor = conexion.cursor()

# Paso 3: Crear una tabla con la columna 'curso'
cursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    edad INTEGER,
                    curso TEXT)''')

# Paso 4: Insertar tres alumnos con nombres, edades y cursos
cursor.execute("INSERT INTO estudiantes (nombre, curso) VALUES ('Lucas', '7°4')")
cursor.execute("INSERT INTO estudiantes (nombre, curso) VALUES ('Ana', '6°3')")
cursor.execute("INSERT INTO estudiantes (nombre, curso) VALUES ('Carlos', '8°2')")

# Paso 5: Guardar los cambios
conexion.commit()

# Paso 6: Cerrar la conexión
conexion.close()
