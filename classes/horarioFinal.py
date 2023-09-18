from datetime import datetime, timedelta #Utilizacion de Tiempos
import matplotlib.pyplot as plt
from classes.controlDatos import ControlDatos
from classes.periodo import Periodo
from classes.advertencia import Advertencia
import json

class HorarioFinal:    

    def __init__(self,nombre,listaPeriodos,duracionPeriodo,cantidadPeriodos,salones):
        self.nombre = nombre
        self.listaPeriodos = listaPeriodos
        self.advertencias = []   
        self.duracionPeriodo = duracionPeriodo  
        self.eficicienciaCursosAsignados = 0    
        self.eficienciaUsabilidadPeriodos = 0   
        self.cantidadPeriodos = cantidadPeriodos
        self.salones = salones

    def addAdvertencia(self,advertencia):
        self.advertencias.append(advertencia)

    def agregarUnaAdvertencia(self,tipo,contenido,tipoAsignacion):        
        advertencia = Advertencia(tipo,contenido,tipoAsignacion)
        self.advertencias.append(advertencia)
    
    def calcularEficiencia(self,cantidadTotalCursos,cursos):
        # La eficiencia sera medida con varios datos la suma de ellos hacen la eficiencia, entre mas alta mejor la eficiencia
        # (Cursos asignados / Todos los cursos) -> Eficiencia de cursos asignados, siempre es 1 o menor que 1, entre mas cercano a 1 mejor        
        # (Cantidad de cursos no asignados / Periodos libres ) -> Eficiencia de usabilidad de periodos, es 1 o menor, si es negativo quiere decir que no habia
        # posibilidad de insertar mas cursos porque faltaban periodos libres, si es negativo entre mas cerca del 0 mas probabilidad de insertar tenia
        cursosAsignados = []
        cantidadCursosAsignados = 0
        cantidadPeriodosLibres = 0
        for periodo in self.listaPeriodos:
            if periodo.curso != None:
                cursosAsignados.append(periodo.curso)
                cantidadCursosAsignados += 1
            else:
                cantidadPeriodosLibres += 1
        
        set1 = set(cursos)
        set2 = set(cursosAsignados)

        # Encontrar elementos en lista1 que no están en lista2
        elementos_no_contenidos = set1 - set2

        # Convertir el resultado de nuevo en una lista
        resultado = list(elementos_no_contenidos)
        for resul in resultado:
            self.agregarUnaAdvertencia(3,"No se logro asignar el curso: " + resul.nombre, 3)

        cantidadCursosNoAsignados = cantidadTotalCursos - cantidadCursosAsignados

        if cantidadTotalCursos == 0:
            cantidadTotalCursos = 0.001

        self.eficicienciaCursosAsignados = cantidadCursosAsignados/cantidadTotalCursos

        posibleUsabilidad = cantidadPeriodosLibres - cantidadCursosNoAsignados

        if cantidadPeriodosLibres == 0:
            cantidadPeriodosLibres = 0.001

        self.eficienciaUsabilidadPeriodos = posibleUsabilidad/cantidadPeriodosLibres

        
            

        print("Calcular eficiencia")


    
    def dibujarHorario(self, control,cantPeriodos):
        print("Dibujando Horario")
        tablaHorario = []
        f1 = [""]
        for s1 in control.salones:
            f1.append(s1.numero)
        tablaHorario.append(f1)

        vecesAgregado = 0
        cantidadSalones = len(control.salones)

        for p2 in cantPeriodos:    
            filaHorario = [p2]    
            for i in range(cantidadSalones):
                #filaHorario.append(control.periodos[i+vecesAgregado].idperiodo)
                periodoDibujar = self.listaPeriodos[i+vecesAgregado]
                if periodoDibujar.curso == None:
                    filaHorario.append(periodoDibujar.idperiodo)  
                else: 
                    filaHorario.append(periodoDibujar.curso.nombre +" \n "+ periodoDibujar.profesor.nombre)        
            vecesAgregado += cantidadSalones
            tablaHorario.append(filaHorario)

        # Hacer la tabla con mathlib
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis ('off')
        table = ax.table(cellText=tablaHorario, loc='center')
        plt.show()