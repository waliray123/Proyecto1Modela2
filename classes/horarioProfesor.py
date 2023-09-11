class HorarioProfesor:

    

    def __init__(self,horarioFinal):
        self.horarioFinal = horarioFinal
        self.periodos = []
    
    def addPeriodo(self,periodo):
        self.periodos.append(periodo)
