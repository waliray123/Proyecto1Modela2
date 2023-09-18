import datetime
import copy
import random
from classes.controlDatos import ControlDatos
from classes.horarioFinal import HorarioFinal
from classes.advertencia import Advertencia

''' codigo que analizara donde estara cada periodo con su horario'''

class AnalizadorHorario:

    def __init__(self,control,semestre,duracionPeriodo,tipoGeneracion,cantidadCorridas,cantPeriodos):        
        self.control = control
        self.analizarEnQueSalonCabeCurso()        
        self.semestreAnalizar = semestre
        self.duracionPeriodo = duracionPeriodo
        self.tipoGeneracion = tipoGeneracion
        self.cantidadCorridas = cantidadCorridas
        self.cantPeriodos = cantPeriodos

    #Analizar en que salon cabria cada curso segun la cantidad de estudiantes
    def analizarEnQueSalonCabeCurso(self):         
        for c1 in self.control.cursos:  
            for s1 in self.control.salones:
                if c1.cantidadEstudiantes <= s1.asientos:
                    c1.addSalonCandidato(s1)

    
            
    #Validar el horario segun el salon con el curso, cantidad de alumnos, y profesor
    def analizarCursoEntreEnPeriodo(self):        
        horariosARetornar = []
        #Por cada curso que se tenga se tratara de asignar a un horario
        # Hay que ordenar los cursos que se asignaran en el semestre
        cursosEnSemestre = self.cursosAOrdenarPorSemestre(self.control.cursos, self.semestreAnalizar)
        cantidadTotalCursosAsignar = len(cursosEnSemestre)
        
        if self.tipoGeneracion == "Ascendente":
            #Primero los ordena por orden ascendente lo cual hace prioridad a los cursos que se inscribieron primero sin tomar en cuenta la prioridad
            cursosOrdenadosAscendente = sorted(cursosEnSemestre, key=lambda x: x.codigo, reverse=False)    
            horarioFinalAscendente = self.crearHorarioFinalCursoMasImportante(cursosOrdenadosAscendente,"Horario ordenado segun cursos ordenados ascendentemente")    
            horarioFinalAscendente.calcularEficiencia(cantidadTotalCursosAsignar,cursosOrdenadosAscendente)
            horariosARetornar.append(horarioFinalAscendente)
        elif self.tipoGeneracion == "Descendente":

            #Luego se utilizan los cursos ordenados Descendentemente
            cursosOrdenadosDescendente = sorted(cursosEnSemestre, key=lambda x: x.codigo, reverse=True)
            horarioFinalDescendente = self.crearHorarioFinalCursoMasImportante(cursosOrdenadosDescendente,"Horario ordenado segun cursos ordenados descendentemente")
            horarioFinalDescendente.calcularEficiencia(cantidadTotalCursosAsignar,cursosOrdenadosDescendente)
            horariosARetornar.append(horarioFinalDescendente)

        elif self.tipoGeneracion == "Prioridad":
            #Despues se utiliza la prioridad de los cursos para llenar estos cursos por prioridad
            cursosOrdenadosPrioridad = sorted(cursosEnSemestre, key=lambda x: x.prioridad, reverse=True)
            for i in range(int(self.cantidadCorridas)):
                cursosAleatorizadosPrioridad = self.aleatorizarCursosPrioridad(cursosOrdenadosPrioridad)
                horarioFinalPrioridad = self.crearHorarioFinalCursoMasImportante(cursosAleatorizadosPrioridad,"Horario ordenado segun cursos ordenados por priodad de forma ascendente")
                horarioFinalPrioridad.calcularEficiencia(cantidadTotalCursosAsignar,cursosAleatorizadosPrioridad)
                horariosARetornar.append(horarioFinalPrioridad)

        elif self.tipoGeneracion == "Cantidad":
            #Ahora se utiliza la cantidad de estudiantes como prioridad, entre mas estudiantes alla mas rapido se asignaran
            cursosOrdenadosCantidadEstudiantes = sorted(cursosEnSemestre, key=lambda x: x.cantidadEstudiantes, reverse=True)
            for i in range(int(self.cantidadCorridas)):
                cursosAleatorizadosCantidad = self.aleatorizarCursosCantidad(cursosOrdenadosCantidadEstudiantes)
                horarioFinalCantidadEstudiantes = self.crearHorarioFinalCursoMasImportante(cursosAleatorizadosCantidad,"Horario ordenado segun cursos ordenados de mayor a menor cantidad de estudiantes")
                horarioFinalCantidadEstudiantes.calcularEficiencia(cantidadTotalCursosAsignar,cursosAleatorizadosCantidad)
                horariosARetornar.append(horarioFinalCantidadEstudiantes)

        return horariosARetornar
    
    
    def aleatorizarCursosPrioridad(self,cursos):
        cursosDevolver = []
        # Diccionario para almacenar las listas agrupadas
        grupos = {}

        # Itera a través de los números
        # Itera a través de las personas
        for curso in cursos:
            prioridad = curso.prioridad
            # Si la edad ya está en el diccionario, agrega la persona a la lista correspondiente
            if prioridad in grupos:
                grupos[prioridad].append(curso)
            else:
                # Si la edad no está en el diccionario, crea una nueva lista con la persona
                grupos[prioridad] = [curso]

        # Ahora grupos contiene las listas de números iguales
        listas_agrupadas = list(grupos.values())

        # Imprime las listas agrupadas
        for lista in listas_agrupadas:
            random.shuffle(lista)
            for elemento in lista:
                cursosDevolver.append(elemento)
        
        return cursosDevolver
    

    def aleatorizarCursosCantidad(self,cursos):
        cursosDevolver = []
        # Diccionario para almacenar las listas agrupadas
        grupos = {}

        # Itera a través de los números
        # Itera a través de las personas
        for curso in cursos:
            cantidadEstudiantes = curso.cantidadEstudiantes
            # Si la edad ya está en el diccionario, agrega la persona a la lista correspondiente
            if cantidadEstudiantes in grupos:
                grupos[cantidadEstudiantes].append(curso)
            else:
                # Si la edad no está en el diccionario, crea una nueva lista con la persona
                grupos[cantidadEstudiantes] = [curso]

        # Ahora grupos contiene las listas de números iguales
        listas_agrupadas = list(grupos.values())

        # Imprime las listas agrupadas
        for lista in listas_agrupadas:
            random.shuffle(lista)
            for elemento in lista:
                cursosDevolver.append(elemento)
        
        return cursosDevolver



        
                
    #En este caso se generara segun el curso es mas importante que la hora, por lo que se encontrara alguien que de el curso sin importar la hora
    def crearHorarioFinalCursoMasImportante(self, cursos,nombreHorarioFinal):
        #Por cada curso se asignara al primer periodo de la lista de periodos segun su disponibilidad (salon: cantEstudiante)junto con un profesor que lo pueda dar
        listaPeriodos1 = self.crearNuevaListaPeriodos(self.control.periodos)
        horarioFinal1 = HorarioFinal(nombreHorarioFinal,listaPeriodos1,self.duracionPeriodo,self.cantPeriodos,self.control.salones)
        cantidadPeriodos = len(listaPeriodos1)
        self.desasignarTodosCursos(cursos)
        #Se realiza 3 veces la asignacion de cursos, 1. Asignar los cursos con profesores obligatorios, 2. Asignar con profesores optativos, 3. Asignar cursos con profesores de la carrera
        #Si se desean solo los primeros 2 cambiar a range(2) en vez de range(3)
        for tipoAsignacion in range(3):
            for curso1 in cursos:
                vecesPasado = 0
                pasar = 0
                if curso1.asignado == 0:
                    if tipoAsignacion == 0:
                        if not curso1.profesoresFijos:
                            pasar = 1 # Pasar porque no tiene profesores fijos 
                    if pasar == 0:
                        seAvisoPeriodoSemesteEnHora = 0
                        hayPeriodoDeSemestreEnHora = 0
                        for periodo1 in listaPeriodos1:                        
                            vecesPasado+=1
                            if periodo1.curso == None:
                                #Revisa que el curso que se va a asignar no este a la misma hora de otro con semestre igual                                
                                if hayPeriodoDeSemestreEnHora <= 0:
                                    hayPeriodoDeSemestreEnHora = self.revisarPeriodoSemestre(periodo1,curso1,listaPeriodos1)
                                if hayPeriodoDeSemestreEnHora <= 0:
                                    if periodo1.salon.asientos >= curso1.cantidadEstudiantes:
                                        estaAsignadoProfesor = self.asignarProfesorAPeriodo(periodo1, curso1, horarioFinal1, tipoAsignacion)
                                        if estaAsignadoProfesor == 0: 
                                            #Si se esta realizando el tipo de asignacion 0 entonces se esta asignando el profesor fijo, si es el 1 se esta asignando un profesor cualquiera                                                                        
                                            periodo1.setCurso(curso1)
                                            curso1.asignado = 1
                                            break
                                        else:
                                            if vecesPasado == cantidadPeriodos:
                                                if tipoAsignacion == 0:
                                                    horarioFinal1.agregarUnaAdvertencia(1,"No se logro asignar un profesor obligatorio al curso: " + curso1.nombre, 1)
                                                elif tipoAsignacion == 1:
                                                    horarioFinal1.agregarUnaAdvertencia(2,"No se logro asignar un profesor optativo al curso: " + curso1.nombre, 1)
                                                elif tipoAsignacion == 2:
                                                    horarioFinal1.agregarUnaAdvertencia(3,"No se logro asignar un ningun profesor al curso: " + curso1.nombre, 1)
                                    else:
                                        horarioFinal1.agregarUnaAdvertencia(1,"No se logro asignar el curso: " + curso1.nombre + " porque por falta de asientos en salon: " + periodo.salon.numero, 2)
                                else:                       
                                    if seAvisoPeriodoSemesteEnHora == 0:
                                        #Advertir sobre que el periodo no se asigno en la hora del periodo1 porque hay un curso del mismo semestre que se asigno antes
                                        seAvisoPeriodoSemesteEnHora = 1
                                        horarioFinal1.agregarUnaAdvertencia(1,"No se logro asignar el curso: " + curso1.nombre + " porque hay un periodo con un curso del mismo semestre asignado a esa hora", 2)
                                    if hayPeriodoDeSemestreEnHora <= 1:
                                        seAvisoPeriodoSemesteEnHora = 0
                            hayPeriodoDeSemestreEnHora -= 1

        return horarioFinal1
    
    def asignarProfesorAPeriodo(self, periodo, curso, horarioFinal,tipoAsignacion):
        profesoresEvaluar = []
        if tipoAsignacion == 0:
            profesoresEvaluar = curso.profesoresFijos
        elif tipoAsignacion == 1:
            profesoresEvaluar = curso.profesoresCandidatos
        elif tipoAsignacion == 2:
            profesoresEvaluar = self.buscarProfesoresDeCarreraQueDenCurso(curso)

        #Aqui se intentara asignar el periodo a un profesor, en pocas palabras se revisa que el profesor no tenga traslape
        for profesor in profesoresEvaluar:
            estaAsignadoElPeriodo = profesor.asignarPeriodoUsado(horarioFinal,periodo)
            if estaAsignadoElPeriodo == 2 or estaAsignadoElPeriodo == 3:
                periodo.setProfesor(profesor)
                if tipoAsignacion == 2:
                    horarioFinal.agregarUnaAdvertencia(2,"Se asigno el profesor: "+profesor.nombre+", al curso:" + curso.nombre + ", por ser solo de la carrera", 1)                                            
                return 0 #Se logro asignar un profesor                   
        return 1 #No se logro asignar ningun profesor        
    

    def asignarCursoAPeriodo(self, curso, listaPeriodo):
        asignado = 0
        for periodo in listaPeriodo:
            if periodo.curso == None:
                if periodo.salon.asientos >= curso.cantidadEstudiantes:
                    periodo.setCurso(curso)
                    asignado = 1
                    return periodo
        if asignado == 0:
            print("Curso"+curso.nombre+"no asignado por falta de salones con asientos suficientes")   
        
        return None
    
    def cursosAOrdenarPorSemestre(self,cursos,semestre):
        cursosDevolver = []
        for curso in cursos:
            if semestre == 0: #PAR
                if (curso.semestre % 2) == 0: 
                    cursosDevolver.append(curso)
            elif semestre == 1: #IMPAR
                if (curso.semestre % 2) != 0:
                    cursosDevolver.append(curso)
        
        return cursosDevolver    
        
    #Esta funcion revisa si en esa hora del periodo no se esta dando un curso con el mismo semestre del que se quiere asignar
    # Retorna 1 si esta 
    def revisarPeriodoSemestre(self,periodo,curso,listaPeriodos):
        periodosMismaHora = []
        posicionPeriodo = 0
        posicionPeriodoFija = 0
        for periodoL in listaPeriodos:
            if periodoL.idHora == periodo.idHora:
                periodosMismaHora.append(periodoL)
                if periodoL == periodo:
                    posicionPeriodoFija = posicionPeriodo
                posicionPeriodo +=1
        
        indiceEncontrado = 0
        for periodoH in periodosMismaHora:
            if periodoH.curso != None:
                if periodoH.curso.semestre == curso.semestre:
                    print(len(periodosMismaHora))
                    print(posicionPeriodoFija)
                    return len(periodosMismaHora) - posicionPeriodoFija

                


        return indiceEncontrado



    def crearNuevaListaPeriodos(self,listaPeriodos):        
        listaNueva = []
        for periodo1 in listaPeriodos:
            listaNueva.append(copy.copy(periodo1))
        return listaNueva

    def desasignarTodosCursos(self,cursos):
        for curso in cursos:
            curso.asignado = 0


    def buscarProfesoresDeCarreraQueDenCurso(self,curso):
        profesoresRetornar = []
        for profesor in self.control.profesores:
            if profesor.carrera == curso.carrera:
                profesoresRetornar.append(profesor)
        return profesoresRetornar



#TODO:
# Por ejemplo si hay un curso con sobrepeso, asignarlo en el salon con mas espacio, hacer un rango de estudiantes
# hacer cursos que tienen salones especificos
# Aleatorizacion 




