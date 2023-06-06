from menu import Menu
from manejadorPersona import ManejadorPersona
from manejadorTallerCapacitacion import ManejadorTallerCapacitacion
from manejadorInscripcion import ManejadorInscripcion

if __name__ == '__main__':
    MTC = ManejadorTallerCapacitacion()
    MI = ManejadorInscripcion()
    MP = ManejadorPersona()
    menu = Menu()
    menu.ejecutar_menu(MTC, MP, MI)
