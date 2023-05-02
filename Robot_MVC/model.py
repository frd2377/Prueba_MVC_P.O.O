class Robot:
    encendido = False

    def __init__(self,posicion_robot:list,posicion_brazo:list):
        self.posicion_robot = posicion_robot
        self.posicion_brazo = posicion_brazo

    def esta_encendido(self):
        return self.encendido

    def encender(self):
        self.encendido = True
        return self.encendido

    def apagar(self):
        self.encendido = False
        return self.encendido
    
    def ver_status(self):
        if self.esta_encendido():
            return print(f'El robot esta encendido su posicion es {self.posicion_robot} y la posicion del brazo robotico es {self.posicion_brazo}\n')
        return print(f'El robot esta apagado su poscicion es {self.posicion_robot} y la posicion del brazo robotico es {self.posicion_brazo}\n')

    def encender_robot(self):
        if self.esta_encendido():
            return print(f'El robot esta encendido\n')
        self.encender()
        print('El robot esta encendiendose...')
        return print(f'Robot encendido\n')
    
    def apagar_robot(self):
        if not self.esta_encendido():
            return print(f'El robot esta apagado\n')
        self.apagar()
        print('El robot esta apagandose...')
        return print(f'Robot apagado\n')
    
    def mover_robot(self):
        if not self.esta_encendido():
            return print(f'El robot esta apagado\n')
        try:
            while True:
                salir = input('Presione 0 para detener el movimiento o enter para seguir>> ')
                if salir == '0':
                    print('Deteniendo...')
                    break
                print('Ingrese las coordenadas a donde desea mover al robot: (x,y)')
                posicionx = float(input('x >> '))
                posiciony = float(input('y >> '))
                self.posicion_robot = [posicionx,posiciony]
        except:
            print('Ha ocurrido un error')
    
    def mover_brazo(self):
        if not self.esta_encendido():
            return print(f'El robot esta apagado\n')
        try:
            while True:
                salir = input('Presione 0 para detener el movimiento o enter para seguir>> ')
                if salir == '0':
                    print('Deteniendo...')
                    break
                print('Ingrese las coordenadas a donde desea moverlo el brazo robotico: (x,y,z)')
                posicionx = float(input('x angulo de elevacion: '))
                posiciony = float(input('y angulo de giro: '))
                posicionz = float(input('z longitud: '))
                self.posicion_brazo = [posicionx,posiciony,posicionz]
                
        except:
            print('Ha ocurrido un error')

    def ver_posicion_brazo(self):
        return print(f'La posicion del brazo robotico es {self.posicion_brazo}\n')
    
    def ver_posicion_robot(self):
        return print(f'La posicion del robot es {self.posicion_robot}\n')