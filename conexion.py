import sqlite3

def getConexion():
    conexion = sqlite3.connect("estudiantes.db")
    conexion.row_factory = sqlite3.Row #estudiantes["nombres"] -> estudiantes [0]
    try:
        yield conexion
    finally:
        conexion.commit()
        conexion.close()

def initDb():
    conexion = sqlite3.connect("estudiantes.db")
    conexion.execute("CREATE TABLE IF NOT EXISTS estudiantes (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)")
    conexion.commit()
    conexion.close()