class TallerCapacitacion:
    __id: int
    __nombre: str
    __vacantes: int
    __monto: float
    
    def __init__(self, id, nombre, vacantes, monto):
        self.__id = id
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__monto = monto
        
    def get_nombre(self):
        return self.__nombre
    
    def get_monto(self):
        return self.__monto
    
    def get_id(self):
        return self.__id
    
    def actualizar_vac(self):
        self.__vacantes -= 1
        
    
