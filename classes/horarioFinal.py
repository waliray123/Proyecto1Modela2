from datetime import datetime, timedelta #Utilizacion de Tiempos
import matplotlib.pyplot as plt
from classes.controlDatos import ControlDatos
from classes.periodo import Periodo
from classes.advertencia import Advertencia
import json

class HorarioFinal:    

    def __init__(self,nombre,listaPeriodos,duracionPeriodo):
        self.nombre = nombre
        self.listaPeriodos = listaPeriodos
        self.advertencias = []   
        self.duracionPeriodo = duracionPeriodo        

    def addAdvertencia(self,advertencia):
        self.advertencias.append(advertencia)

    def agregarUnaAdvertencia(self,tipo,contenido,tipoAsignacion):        
        advertencia = Advertencia(tipo,contenido,tipoAsignacion)
        self.advertencias.append(advertencia)
    
    def calcularEficiencia(self):
        # La eficiencia sera medida con varios datos la suma de ellos hacen la eficiencia, entre mas alta mejor la eficiencia
        # (Cursos asignados / Todos los cursos) -> Eficiencia de cursos asignados
        # (Periodos libres / Cantidad de cursos no asignados) -> Eficiencia de usabilidad de periodos        


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