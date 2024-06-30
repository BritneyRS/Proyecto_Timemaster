import unittest
# test/test_negocio.py

import pytest
from datetime import time
from src.logica.logicaAlarma import crear_usuario, crear_alarma, obtener_usuarios, obtener_alarmas, cerrar_sesion
from src.modelo.declarative_base import Base, engine, Session

# Crear una nueva sesión para pruebas
session = Session()

@pytest.fixture(scope='module')
def setup_database():
    # Crear todas las tablas
    Base.metadata.create_all(engine)
    yield
    # Eliminar todas las tablas después de las pruebas
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def session_scope():
    """ Proporcionar una nueva sesión para cada prueba """
    new_session = Session()
    yield new_session
    new_session.close()

def test_crear_usuario(setup_database, session_scope):
    usuario = crear_usuario('Test User', 'test@example.com')
    usuarios = obtener_usuarios()
    assert len(usuarios) == 1
    assert usuarios[0].nombre == 'Test User'
    assert usuarios[0].email == 'test@example.com'

def test_crear_alarma(setup_database, session_scope):
    usuario = crear_usuario('Test User', 'test@example.com')
    alarma = crear_alarma(time(6, 0), 'Prueba de alarma', usuario.id)
    alarmas = obtener_alarmas()
    assert len(alarmas) == 1
    assert alarmas[0].hora == time(6, 0)
    assert alarmas[0].descripcion == 'Prueba de alarma'
    assert alarmas[0].usuario_id == usuario.id

@pytest.fixture(scope='function', autouse=True)
def cleanup_database():
    # Limpiar la base de datos antes de cada prueba
    session.rollback()
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()

# Cierra la sesión después de todas las pruebas
def test_cerrar_sesion():
    cerrar_sesion()





if __name__ == '__main__':
    unittest.main()
