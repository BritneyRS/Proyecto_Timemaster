# modelo/models.py

from sqlalchemy import create_engine, Column, Integer, String, Time, ForeignKey
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from src.modelo.declarative_base import Base,engine


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    alarmas = relationship('Alarma', back_populates='usuario')

class Alarma(Base):
    __tablename__ = 'alarmas'
    id = Column(Integer, primary_key=True)
    hora = Column(Time, nullable=False)
    descripcion = Column(String, nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('Usuario', back_populates='alarmas')


Base.metadata.create_all(engine)
