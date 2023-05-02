#Frd
from os import system

class Robot_View:
    def main(self):
        while True:
            print('**Robot**')
            print('Ingrese la accion a realizar: ')
            print('1.- Ver informacion\n2.- Encender\n3.- Apagar\n4.- Mover Robot\n5.- Mover brazo robotico\n6.- Ver posicion brazo\n7.- Ver posicion robot\n8.- Salir')
            accion = input('>> ')
            system('cls')

            if accion == '1':
                self.controller.ver_status()

            if accion == '2':
                self.controller.encender_robot()

            if accion == '3':
                self.controller.apagar_robot()

            if accion == '4':
                self.controller.mover_robot()

            if accion == '5':
                self.controller.mover_brazo()

            if accion == '6':
                self.controller.ver_posicion_brazo()

            if accion == '7':
                self.controller.ver_posicion_robot()

            if accion == '8':
                break

