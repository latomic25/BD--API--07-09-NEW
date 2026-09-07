from models.modelo import Estudiante
from sqlite3 import Connection

class manager_estudiante:
    def __init__(self):
        pass

    def post_estudiante(self,estudiante: Estudiante,conexion: Connection):
        conexion.execute("INSERT INTO estudiantes (nombre, apellido) VALUES (?,?)", (estudiante.nombre, estudiante.apellido))
        return f"Estudiante agregado: {estudiante.nombre} {estudiante.apellido}!"

    def get_estudiante(self,conexion):
        res = conexion.execute("SELECT * FROM estudiantes").fetchall()
        return [dict(item) for item in res]

    def delete_estudiante(self,conexion, id):
        conexion.execute("DELETE FROM estudiantes WHERE id = ?",(id,))
        return "Estudiante eliminado!"

    def put_estudiante(self,conexion, nombre, id):
        conexion.execute("UPDATE estudiantes SET nombre = ? WHERE id = ?",(nombre,id))
        return "Se ha cambiado el nombre perfectamente!"