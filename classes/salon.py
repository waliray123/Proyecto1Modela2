class Salon:

    def __init__(self,numero,asientos):
        self.numero = numero
        self.asientos = asientos
        self.carreraEspecifica = None
        self.posicionNueva = 0

    def setCarreraEspecifica(self,carrera):
        self.carreraEspecifica = carrera

    def setPosicion(self,posicion):
        self.posicionNueva = posicion
        