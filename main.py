from fastapi import FastAPI, Depends
from conexion import getConexion, initDb
from models.modelo import Estudiante
import sqlite3
from manager.manager_est import manager_estudiante

manager_estudiante = manager_estudiante()
app = FastAPI()

@app.on_event("startup")
def startup():
    initDb()

@app.post("/agregar_estudiante")
def agregarEstudiante(estudiante: Estudiante, conexion: sqlite3.Connection = Depends(getConexion)):
    return manager_estudiante.post_estudiante(estudiante,conexion)

@app.get("/leer_estudiantes")
def leerEstudiantes(conexion: sqlite3.Connection = Depends(getConexion)):
    return manager_estudiante.get_estudiante(conexion)

@app.delete("/eliminar_estudiante/{id}")
def eliminarEstudiante(id: int, conexion: sqlite3.Connection = Depends(getConexion)):
    return manager_estudiante.delete_estudiante(conexion,id)

@app.put("/actualizar_estudiante/{id}")
def actualizarEstudiante(nombre:str,id: int, conexion: sqlite3.Connection = Depends(getConexion)):
    return manager_estudiante.put_estudiante(conexion,nombre, id)