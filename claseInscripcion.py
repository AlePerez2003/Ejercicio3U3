from clasePersona import Persona
from claseTallerCapacitacion import TallerCapacitacion

class Inscripcion:
    __fecha_inscripcion: str
    __pago: bool
    __persona: Persona
    __taller: TallerCapacitacion
    
    def __init__(self, fecha, persona, taller, pago = False):
        self.__fecha_inscripcion = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller
        
    def get_dni(self):
        return self.__persona.get_dni()
    
    def get_nombre_taller(self):
        return self.__taller.get_nombre()
    
    def get_pago(self):
        return self.__pago
    
    def get_monto(self):
        return self.__taller.get_monto()
    
    def get_id(self):
        return self.__taller.get_id()
    
    def get_fecha(self):
        return self.__fecha_inscripcion
    
    def get_datos_inscripto(self):
        return self.__persona.get_nombre() + '' + self.__persona.get_direccion() + '' + self.__persona.get_dni()
    
    def actualizar_pago(self):
        self.__pago = True
        
        
    