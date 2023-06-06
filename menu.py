from manejadorPersona import ManejadorPersona
from manejadorTallerCapacitacion import ManejadorTallerCapacitacion
from manejadorInscripcion import ManejadorInscripcion

class Menu:
    __cod: int
    
    def mostrar_menu(self):
        print('Opcion 1: Cargar los datos de los talleres ')
        print('Opcion 2: Inscribir una persona en un taller')
        print('Opcion 3: Consultar inscripción')
        print('Opcion 4: Consultar inscriptos')
        print('Opcion 5: Registrar pago')
        print('Opcion 6: Guardar inscripciones')
        print('Opcion 0: Finalizar operación')
        
    def ejecutar_menu(self, MTC: ManejadorTallerCapacitacion, MP: ManejadorPersona, MI: ManejadorInscripcion):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el codigo'))
        while self.__cod != 0:
            if self.__cod == 1:
                MTC.cargar_talleres()
            elif self.__cod == 2:
                MI.cargar_inscripcion(MTC, MP)
            elif self.__cod == 3:
                MI.mostrar_datos()
            elif self.__cod == 4:
                MI.mostrar_por_taller(MTC)
            elif self.__cod == 5:
                MI.registrar_pago()
            elif self.__cod == 6:
                MI.guardar_inscripciones()
            else:
                print('Codigo Incorrecto')
            self.mostrar_menu()
            self.__cod = int(input('Ingrese el codigo'))
        