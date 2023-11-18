import sqlite3
def connexion():
        conexion = sqlite3.connect("baseturnos.db")

        cursor = conexion.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        edad INT (5),
        telefono INT(20),
        dni INT(20),
        direccion VARCHAR(50),
        correo VARCHAR(50),
        obrasocial INTEGER,
        sexo VARCHAR(10)
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS profesionales (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        dni INT(20),
        numero INT(20),
        correo VARCHAR(50),
        especialidad VARCHAR(50),
        direccion VARCHAR(50))
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS turnos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        profesional_id INTEGER,
        fecha VARCHAR(10),
        FOREIGN KEY (paciente_id) REFERENCES pacientes (ID),
        FOREIGN KEY (profesional_id) REFERENCES profesionales (ID)
                )
     ''')
        conexion.close()
 
connexion()