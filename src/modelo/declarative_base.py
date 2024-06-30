from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

# Configuración de la base de datos
engine = create_engine('sqlite:///despertar.db')
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()