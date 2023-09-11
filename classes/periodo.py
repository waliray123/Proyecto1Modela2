class Periodo:    

    

    def __init__(self,horario,salon,idperiodo,idHora,idSalon):        
        self.horario = horario
        self.salon = salon
        self.idperiodo = idperiodo
        self.idHora = idHora
        self.idSalon = idSalon
        self.curso = None
        self.profesor = None

    def setCurso(self, curso):
        self.curso = curso

    def setProfesor(self, profesor):
        self.profesor = profesor
    
    def getHoraEnString(self):
        return self.horario.horaInicial.strftime("%H:%M:%S") + " - " + self.horario.horaFinal.strftime("%H:%M:%S")


