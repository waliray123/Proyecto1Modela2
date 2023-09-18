from datetime import datetime, timedelta #Utilizacion de Tiempos
import matplotlib.pyplot as plt
from classes.analizador import AnalizadorHorario
from datos import mockD 
import importlib

class Inicializador:

    def __init__(self,tipoGeneracion,cantidadCorridas,duracionPeriodo,semestreUsar,strHoraI,strHoraF):                  
        try:
            importlib.reload(mockD)
            print('Módulo "mockD" recargado exitosamente.')
        except ImportError:
            print('No se pudo encontrar el módulo "mockD".')
        except Exception as e:
            print(f'Error al recargar el módulo "mockD": {e}')
        
        from datos.mockD import MockData #Carga de datos  
            
        """Cargar los datos necesarios: Cursos, Estudiantes, Profesores, Salones"""
        cargarDatos = MockData()
        control = cargarDatos.analizarDatos()

        """Definir el tiempo de los periodos en minutos"""
        #duracionPeriodo = 50

        """Definir la hora de inicio y final de todo el horario laboral"""
        #horaInicialLaboral = datetime.strptime("7:00 AM", "%I:%M %p")
        #horaFinalLaboral = datetime.strptime("1:00 PM", "%I:%M %p")
        horaInicialLaboral = datetime.strptime(strHoraI, "%I:%M %p")
        horaFinalLaboral = datetime.strptime(strHoraF, "%I:%M %p")


        """Definir el semestre en el que se esta trabajando; 0 = par 1 = impar"""
        semestre = 0
        if semestreUsar == "PAR":
            semestre = 0
        elif semestreUsar == "IMPAR":
            semestre = 1
            
        

        """Generar tabla de periodos/salon"""

        #Calcular la cantidad de periodos en el horario laboral
        self.listaPeriodos = self.calcular_periodos(horaInicialLaboral,horaFinalLaboral,duracionPeriodo)
        #cantPeriodos = len(listaPeriodos)

        #Hacer la tabla de periodos
        idperiodo = 0
        idperiodoSalon = 0
        for p1 in self.listaPeriodos:     
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
        analizadorHorario = AnalizadorHorario(control,semestre,duracionPeriodo,tipoGeneracion,cantidadCorridas,self.listaPeriodos)
        self.horariosRetornados = analizadorHorario.analizarCursoEntreEnPeriodo()
        self.control1 = control 

        '''
        for horarioR in horariosRetornados:
            horarioR.dibujarHorario(control,self.listaPeriodos)
        '''
        print("terminados")
    
    def calcular_periodos(self,inicio, fin, duracion_periodo):
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









