class Persona:
    __nombre: str
    __direccion: str
    __dni: str
    
    def __init__(self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
        
    def get_dni(self):
        return self.__dni
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion