import numpy as np
from numpy import ndarray
import csv
from claseInscripcion import Inscripcion
from clasePersona import Persona
from manejadorTallerCapacitacion import ManejadorTallerCapacitacion
from manejadorPersona import ManejadorPersona

class ManejadorInscripcion:
    __cantidad: int
    __incremento: int
    __inscripciones: ndarray
    __dimension: int
    
    def __init__(self, cantidad = 10, incremento = 10, dimension = 10):
        self.__cantidad = 0
        self.__incremento = incremento
        self.__dimension = dimension
        self.__inscripciones = np.empty(self.__dimension, dtype = Inscripcion)
        
    def cargar_inscripcion(self, MTC:ManejadorTallerCapacitacion, MP:ManejadorPersona):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__inscripciones.resize(self.__dimension)
        else:
            print('Ingrese los datos de la Persona a inscribir')
            nombre = input('Ingrese el Nombre')
            direccion = input('Ingrese la dirección')
            dni = input('Ingrese el DNI')
            unaPersona = Persona(nombre, direccion, dni)
            
            MTC.mostrar_talleres()
            ind = int(input('Ingrese el ID del taller a inscribirse'))
            unTaller = MTC.get_taller(ind-1)
            MTC.act_vacante(ind-1)
            
            Fecha = input('Ingrese la Fecha de inscripcion')
            unaInscripcion = Inscripcion(Fecha, unaPersona, unTaller)
            MP.cargar_persona(unaPersona)
            self.__inscripciones[self.__cantidad] = unaInscripcion
            self.__cantidad += 1
            
    def buscar_por_persona(self, dni):
        bandera = False
        i = 0
        while i < self.__cantidad and not bandera:
            if self.__inscripciones[i].get_dni() == dni:
                bandera = True
            else: 
                i += 1
            return i
        
    def mostrar_datos(self):
        dni = input('Ingrese el DNI a consultar')
        ind = self.buscar_por_persona(dni)
        if ind == self.__cantidad:
            print('La persona no esta inscripta')
        else:
            print('Taller Inscripto: ' + self.__inscripciones[ind].get_nombre_taller())
            if self.__inscripciones[ind].get_pago() == False:
                print('Monto que adeuda: {}'.format(self.__inscripciones[ind].get_monto()))
                
    def mostrar_por_taller(self, MTC:ManejadorTallerCapacitacion):
        MTC.mostrar_talleres()
        id = int(input('Ingrese un ID de Taller'))
        for i in range(self.__cantidad):
            if self.__inscripciones[i].get_id() == id:
                print(self.__inscripciones[i].get_datos_inscripto())
                
    def registrar_pago(self):
        dni = input('Ingrese el DNI a registrar el pago')
        ind = self.buscar_por_persona(dni)
        if ind == self.__cantidad:
            print('La persona no esta inscripta')
        else:
            self.__inscripciones[ind].actualizar_pago()
            print('El pago se actualizo exitosamente')
            
    def guardar_inscripciones(self):
        archivo = open('Inscripciones.csv', 'w', newline = '')
        writer = csv.writer(archivo)
        for i in range(self.__cantidad):
            dni = self.__inscripciones[i].get_dni()
            idtaller = self.__inscripciones[i].get_id()
            fecha = self.__inscripciones[i].get_fecha()
            pago = self.__inscripciones[i].get_pago()
            newfila = [dni,idtaller,fecha,pago]
            writer.writerow(newfila)
        archivo.close