class Curso:

    

    def __init__(self,codigo,nombre,creditos,semestre,duracion,carrera,cantidadEstudiantes,color):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.semestre = semestre
        self.duracion = duracion
        self.carrera = carrera
        self.cantidadEstudiantes = cantidadEstudiantes
        self.profesoresCandidatos = []
        self.salonesCandidatos = []
        self.prioridad = 0
        self.profesoresFijos = []
        self.asignado = 0
        self.salonEspecifico = []
        self.color = color

    def addProfesorCandidato(self,profesor):
        self.profesoresCandidatos.append(profesor)

    def addProfesorFijo(self,profesor):
        self.profesoresFijos.append(profesor)

    def addSalonCandidato(self,salon):
        self.salonesCandidatos.append(salon)

    def setPrioridad(self,prioridad):
        self.prioridad = prioridad
    
    def addSalonEspecifico(self,salon):
        self.salonEspecifico.append(salon)

    
