from mockData import control #Carga de datos
from datetime import datetime, timedelta #Utilizacion de Tiempos
import matplotlib.pyplot as plt
from classes.analizador import AnalizadorHorario

"""Cargar los datos necesarios: Cursos, Estudiantes, Profesores, Salones"""

"""Definir el tiempo de los periodos en minutos"""
duracionPeriodo = 50

"""Definir la hora de inicio y final de todo el horario laboral"""
horaInicialLaboral = datetime.strptime("7:00 AM", "%I:%M %p")
horaFinalLaboral = datetime.strptime("1:00 PM", "%I:%M %p")

"""Definir el semestre en el que se esta trabajando; 0 = par 1 = impar"""
semestre = 1

"""Generar tabla de periodos/salon"""
def calcular_periodos(inicio, fin, duracion_periodo):
    # Convertir las horas iniciales y finales a minutos
    inicioMinutos = (inicio.hour * 60) + inicio.minute
    finMinutos = (fin.hour * 60) + fin.minute
    
    # Calcular la duración total en minutos
    duracionTotal = finMinutos - inicioMinutos
    
    # Calcular la cantidad de periodos completos
    periodosCompletos = duracionTotal // duracion_periodo
    
    periodosLista = []
    for i in range(periodosCompletos):
        periodoInicio = inicio + timedelta(minutes=i * duracion_periodo)
        periodoFin = inicio + timedelta(minutes=(i + 1) * duracion_periodo)
        periodosLista.append((periodoInicio.strftime("%I:%M %p"), periodoFin.strftime("%I:%M %p")))
    
    return periodosLista

#Calcular la cantidad de periodos en el horario laboral
listaPeriodos = calcular_periodos(horaInicialLaboral,horaFinalLaboral,duracionPeriodo)
#cantPeriodos = len(listaPeriodos)

#Hacer la tabla de periodos
idperiodo = 0
idperiodoSalon = 0
for p1 in listaPeriodos:     
    idperiodo += 10
    idperiodoSalon = 0
    for s1 in control.salones:
        idperiodoSalon += 1
        hora1 = datetime.strptime(p1[0], "%I:%M %p")
        hora2 = datetime.strptime(p1[1], "%I:%M %p")
        control.setPeriodo([hora1,hora2], s1, (idperiodo+idperiodoSalon),idperiodo,idperiodoSalon)


"""Llenar periodos que no se usaran o que estan limitados de uso a cierta hora"""
#Hacer un curso predeterminado que funcione para llenar o limitar
#control.setCurso(000, "Limitado", 0, 0, 0, 0, 0)
#TODO: realizar las limitaciones a una hora determinada o varias horas

"""Llenar la tabla de periodos/salon"""
#Analizar el horario
analizadorHorario = AnalizadorHorario(control,semestre,duracionPeriodo)
horariosRetornados = analizadorHorario.analizarCursoEntreEnPeriodo()

'''
for horarioR in horariosRetornados:
    horarioR.dibujarHorario(control,listaPeriodos)
'''


print("terminados")




    
        



