import csv
from clasePersona import Persona

class ManejadorPersona:
    __personas: list
    
    def __init__(self):
        self.__personas = []
        
    def cargar_persona(self, unaPersona):
        self.__personas.append(unaPersona)