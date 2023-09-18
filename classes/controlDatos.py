from classes.curso import Curso
from classes.carrera import Carrera
from classes.salon import Salon
from classes.estudiante import Estudiante
from classes.horario import Horario
from classes.profesor import Profesor
from classes.periodo import Periodo
import random


class ControlDatos:

    def __init__(self):                
        print("Inicializacion de controlador")   
        self.cursos = []
        self.salones = []    
        self.estudiantes = []
        self.horarios = []
        self.profesores = []
        self.periodos = []
        self.carreras = [] 

    def setCarrera(self,codigo,nombre): 
        # Genera valores RGB aleatorios
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        # Formatea el color en formato hexadecimal
        color_hex = "#{:02x}{:02x}{:02x}".format(red, green, blue)
        print("Color aleatorio:", color_hex) 
        c1 = Carrera(codigo, nombre,color_hex)
        self.carreras.append(c1)    

    def setCurso(self,codigo,nombre,creditos,semestre,duracion,carrera,cantidadEstudiantes):
        c1 = self.buscarCarreraPorCodigo(carrera)
        if c1 == 0:
            print("No se pudo ingresar la carrera ya que no existe una con codigo: " + str(carrera))
            carreraExtra = Carrera(0, "No se asigno carrera","#FF0000")
            c2 = Curso(codigo,nombre,creditos,semestre,duracion,carreraExtra,cantidadEstudiantes,"#FF0000")
        else:
            c2 = Curso(codigo,nombre,creditos,semestre,duracion,c1,cantidadEstudiantes,c1.color)
        self.cursos.append(c2)

    def setSalon(self,numero,asientos):
        s1 = Salon(numero,asientos)
        self.salones.append(s1)      
      

    def setEstudiante(self, nombre,cursosGanados,cursosPorLlevar):
        cursosG = []
        cursosPL = []
        for cursoGanado in cursosGanados:
            cursoG = self.buscarCursoPorCodigo(cursoGanado)
            if cursoG != 0:
                cursosG.append(cursoG)
        
        for cursoPorLlevar in cursosPorLlevar:
            cursoPL = self.buscarCursoPorCodigo(cursoPorLlevar)
            if cursoPL != 0:
                cursosPL.append(cursoPL)

        e1 = Estudiante(nombre,cursosG,cursosPL)
        self.estudiantes.append(e1)

    def setHorarioContratacion(self,horaInicial,horaFinal):
        h1 = Horario(horaInicial, horaFinal)
        self.horarios.append(h1)
        return h1
    
    def setProfesor(self, nombre,cursosPuedeDar,horarioContratacion,carrera):        
        cursosPD = []
        
        for cursoPuedeDar in cursosPuedeDar:
            cursoPD = self.buscarCursoPorCodigo(cursoPuedeDar)
            if cursoPD != 0:                
                cursosPD.append(cursoPD)

        c1 = self.buscarCarreraPorCodigo(carrera)

        p1 = Profesor(nombre, cursosPD, self.buscarHorario(horarioContratacion),c1)        
        self.profesores.append(p1)
        for cursoPD in cursosPD:
            cursoPD.addProfesorCandidato(p1)
    
    def setProfesorFijoACurso(self,nombreProfesor,codigoCurso):
        profesor = self.buscarProfesorPorNombre(nombreProfesor)
        curso = self.buscarCursoPorCodigo(codigoCurso)
        curso.addProfesorFijo(profesor)


    def setPeriodo(self,horaPeriodo,salon,idperiodo,idHora,idSalon):        
        horario = self.buscarHorario(horaPeriodo)
        p1 = Periodo(horario, salon, idperiodo, idHora, idSalon)
        self.periodos.append(p1)
    
    def buscarHorario(self,horarioContratacion):
        horarioNuevo = 1;
        for horario in self.horarios:
            if horario.horaInicial == horarioContratacion[0]:
                if horario.horaFinal == horarioContratacion[1]:                    
                    return horario

        if horarioNuevo == 1:
            horarioN = self.setHorarioContratacion(horarioContratacion[0], horarioContratacion[1])
            return horarioN    
    
    def setPrioridadCurso(self,codigoCurso,priodad):
        cursoPonerPrioridad = self.buscarCursoPorCodigo(codigoCurso)
        cursoPonerPrioridad.setPrioridad(priodad)

    def setSalonEspecifico(self,codigoSalon,codigoCurso):
        cursoPonerSalon = self.buscarCursoPorCodigo(codigoCurso)
        salonAPoner = self.buscarSalonPorCodigo(codigoSalon)
        cursoPonerSalon.addSalonEspecifico(salonAPoner)
    
    def buscarSalonPorCodigo(self,codigoSalon):
        for salon in self.salones:
            if salon.numero == codigoSalon:
                return salon
        return 0
    
    def buscarCursoPorNombre(self,nombre):
        for curso in self.cursos:
            if curso.nombre == nombre:
                return curso
        return 0

    def buscarCursoPorCodigo(self,codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return 0

    def buscarProfesorPorNombre(self,nombre):
        for profesor in self.profesores:
            if profesor.nombre == nombre:
                return profesor
        return 0

    def buscarCarreraPorCodigo(self,codigo):
        for carrera in self.carreras:
            if carrera.codigo == codigo:
                return carrera
        return 0