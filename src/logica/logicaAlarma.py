# logica/negocio.py

from src.modelo.declarative_base import Session
from src.modelo.modeloAlarma import Usuario, Alarma

# Crear una nueva sesión
session = Session()

def crear_usuario(nombre, email):
    nuevo_usuario = Usuario(nombre=nombre, email=email)
    session.add(nuevo_usuario)
    session.commit()
    return nuevo_usuario

def crear_alarma(hora, descripcion, usuario_id):
    nueva_alarma = Alarma(hora=hora, descripcion=descripcion, usuario_id=usuario_id)
    session.add(nueva_alarma)
    session.commit()
    return nueva_alarma

def obtener_usuarios():
    return session.query(Usuario).all()

def obtener_alarmas():
    return session.query(Alarma).all()

# Cierra la sesión cuando ya no sea necesaria
def cerrar_sesion():
    session.close()
