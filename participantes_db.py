import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Registros(Base):
    __tablename__ = 'registros'

    id = Column(Integer(), primary_key = True)
    nombre = Column(String(80), nullable = False) 
    apellido = Column(String(80), nullable = False) 
    edad = Column(Integer(), nullable = False) 
    sexo = Column(String(), nullable = False)
    disp1 = Column(Float, nullable = False)
    disp2 = Column(Float, nullable = False)
    disp3 = Column(Float, nullable = False)
    mejor_disparo = Column(Float, nullable = False)
    promedio_participante = Column(Float, nullable = False) 

    def __init__(self, id, nombre, apellido, edad, sexo, disp1, disp2, disp3, mejor_disparo, promedio_participante):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.disp1 = disp1
        self.disp2 = disp2
        self.disp3 = disp3
        self.mejor_disparo = mejor_disparo
        self.promedio_participante = promedio_participante
        
    def __str__(self):
        return "Participante:\nId: {}\nNombre: {}\nApellido: {}\nEdad: {}\nSexo: {}\nPrimer disparo: {}\nSegundo disparo: {}\nTercer disparo: {}\nMejor disparo: {}\nPromedio: {}\n".format(self.id, self.nombre, self.apellido, self.edad, self.sexo, self.disp1, self.disp2, self.disp3, self.mejor_disparo, self.promedio_participante)


engine = create_engine('sqlite:///participantes.db')
Base.metadata.create_all(engine)