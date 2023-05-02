class Robot_Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view
    
    def ver_status(self):
        return self.model.ver_status()

    def encender_robot(self):
        return self.model.encender_robot()
    
    def apagar_robot(self):
        return self.model.apagar_robot()
    
    def mover_robot(self):
        return self.model.mover_robot()
    
    def mover_brazo(self):
        return self.model.mover_brazo()

    def ver_posicion_brazo(self):
        return self.model.ver_posicion_brazo()
    
    def ver_posicion_robot(self):
        return self.model.ver_posicion_robot()