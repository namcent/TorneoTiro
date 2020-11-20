from math import sqrt
import csv
import requests
from participantes_db import Registros, Base, engine
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Participante():
    contador = 0
    def __init__(self, nombre, apellido, edad, sexo):
        Participante.contador += 1
        self.id= Participante.contador
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.sexo=sexo
    
    def __str__(self):
        return 'Participante:\nId: {}\nNombre: {}\nApellido: {}\nEdad: {}\nSexo: {}\n'.format(self.id, self.nombre, self.apellido, self.edad, self.sexo)

    
class Disparo(Participante):
    def __init__(self, nombre, apellido, edad, sexo, posiciones = []):
        Participante.__init__(self, nombre, apellido, edad, sexo)
        self.posiciones = posiciones
        self.disp1=round(float(sqrt(self.posiciones[0]**2 + self.posiciones[1]**2)), 2)
        self.disp2=round(float(sqrt(self.posiciones[2]**2 + self.posiciones[3]**2)), 2)
        self.disp3=round(float(sqrt(self.posiciones[4]**2 + self.posiciones[5]**2)), 2)
        self.disparos=[self.disp1, self.disp2, self.disp3]
        self.mejor_disparo = sorted(self.disparos)[0]
        self.promedio_participante = round((sum(self.disparos)/3), 2)
        self.peor_disparo = sorted(self.disparos)[-1]
        
    def __str__(self):
        return 'Participante:\nId: {}\nNombre: {}\nApellido: {}\nEdad: {}\nSexo: {}\nDisparos: {}\nMejor disparo: {}\nPromedio disparos: {}\n'.format(
                self.id, self.nombre, self.apellido, self.edad, self.sexo, self.disparos, self.mejor_disparo, self.promedio_participante)


class Concurso():
    participantes = []

    def agregar(self, disparo):
        self.participantes.append(disparo)

    def mostrar_registros(self):
        for participante in self.participantes:
            print (participante)

    def mostrar_cantidad_participantes(self):
        cantidad = 0
        for participante in self.participantes:
            cantidad += 1
        print("La cantidad de participantes es {}".format(cantidad))

    def mostrar_ganador(self):
        mejor_disparo = 9999999
        for participante in self.participantes:
            disparo = participante.mejor_disparo
            if disparo < mejor_disparo:
                ganador = participante.nombre
                mejor_disparo = disparo
        print("El ganador es {}".format(ganador))

    def mostrar_podio(self):
        podio = []
        for i in range(len(self.participantes)-1):
            for k in range(len(self.participantes)-1-i):
                if self.participantes[ k ].mejor_disparo > self.participantes[ k+1 ].mejor_disparo:
                    self.participantes[ k ],self.participantes[ k+1 ] = self.participantes[ k+1 ],self.participantes[ k ]
        while len(podio) < 3:
            for participante in self.participantes:
                podio.append(participante.nombre)
        print("El podio es: \n{}".format(podio))        

    def mostrar_ultimo(self):
        for i in range(len(self.participantes)-1):
            for k in range(len(self.participantes)-1-i):
                if self.participantes[ k ].mejor_disparo > self.participantes[ k+1 ].mejor_disparo:
                    self.participantes[ k ],self.participantes[ k+1 ] = self.participantes[ k+1 ],self.participantes[ k ]
        print("El ultimo puesto es de {}".format(self.participantes[-1].nombre))

    def ordenar_por_edad(self):
        for i in range(len(self.participantes)-1):
            for k in range(len(self.participantes)-1-i):
                if self.participantes[ k ].edad > self.participantes[ k+1 ].edad:
                    self.participantes[ k ],self.participantes[ k+1 ] = self.participantes[ k+1 ],self.participantes[ k ]
        for participante in self.participantes:
            print(participante)

    def mostrar_promedio(self):
        promedios = 0
        cantidad = 0
        for participante in self.participantes:
            promedios = promedios + participante.promedio_participante
            cantidad += 1
        print("El promedio total es {}".format(round(promedios/cantidad, 2)))

    def guardar_csv(self):
        with open('participantes.csv', 'w') as archivo:
            for participante in self.participantes:
                archivo_csv = csv.writer(archivo)
                registro = [participante.id, participante.nombre, participante.apellido, participante.edad, participante.disparos, participante.mejor_disparo, participante.promedio_participante]
                archivo_csv.writerow(registro)
        print("Los datos han sido guardados correctamente.")
            
    def guardar_db(self):
        for participante in self.participantes:
            id = participante.id
            nombre = participante.nombre
            apellido = participante.apellido
            edad = participante.edad
            sexo = participante.sexo
            disp1 = participante.disp1
            disp2 = participante.disp2
            disp3 = participante.disp3
            mejor_disparo = participante.mejor_disparo
            promedio_participante = participante.promedio_participante

            registro = Registros(id, nombre, apellido, edad, sexo, disp1, disp2, disp3, mejor_disparo, promedio_participante)
            session.add(registro)
            session.commit()
        print("Los datos han sido guardados correctamente en la base de datos.")

    def mostrar_db(self):
        registros = session.query(Registros).all()
        for participante in registros:
            print(participante)

    def mostrar_premio(self):
        mejor_disparo = 9999999
        for participante in self.participantes:
            disparo = participante.mejor_disparo
            if disparo < mejor_disparo:
                ganador = participante.nombre
                mejor_disparo = disparo
        url = "http://13.58.21.137/flask/api/v2/{}/{}".format(ganador, mejor_disparo)
        response = requests.get(url)
        responseJSON = response.json()
        premio = responseJSON['premio']
        nombre = responseJSON['nombre']
        print("El premio de {} es {}".format(nombre, premio))
