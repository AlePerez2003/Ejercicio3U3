import csv
import numpy as np
from numpy import ndarray
from claseTallerCapacitacion import TallerCapacitacion

class ManejadorTallerCapacitacion:
    __dimension: int
    __cantidad: int
    __talleres: ndarray
    __incremento: int
    
    def __init__(self, cantidad = 0, incremento = 5):
        self.__cantidad = cantidad
        self.__incremento = incremento
        
    def cargar_talleres(self):
        bandera = False
        with open('Talleres.csv', 'r')as file:
            reader = csv.reader(file, delimiter = ';')
            for fila in reader:
                if bandera == False:
                    bandera = True
                    cantidad = int(fila[0])
                    self.__talleres = np.empty(cantidad, dtype = TallerCapacitacion)
                else:
                    self.__talleres[self.__cantidad] = TallerCapacitacion(int(fila[0]), fila[1], int(fila[2]), float(fila[3]))
                    self.__cantidad += 1
                    
    def mostrar_talleres(self):
        for i in range(self.__cantidad):
            print('{}) Nombre: '.format(i+1) + self.__talleres[i].get_nombre())
    
    def get_taller(self, ind):
        return self.__talleres[ind]
    
    def act_vacante(self, ind):
        self.__talleres[ind].actualizar_vac()