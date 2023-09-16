from classes.horarioProfesor import HorarioProfesor

class Profesor:        

    def __init__(self,nombre,cursosPuedeDar,horarioContratacion,carrera):
        self.nombre = nombre
        self.cursosPuedeDar = cursosPuedeDar
        self.horarioContratacion = horarioContratacion
        self.horariosUsados = []
        self.carrera = carrera
    

    def asignarPeriodoUsado(self, horarioFinal ,periodo):
        horarioEncontrado = None
        periodoEncontrado = 0
        #validar que el profesor esta en hora de trabajo 
        estaEnHoraLaboral = self.calcularEstaDentroHoraDeContratacion(periodo,horarioFinal.duracionPeriodo)
        #TODO: Advertir que no esta en hora de trabajo
        if estaEnHoraLaboral == 1:
            for horariosUsado in self.horariosUsados:
                if horarioFinal == horariosUsado.horarioFinal:                
                    horarioEncontrado = horariosUsado
                    listaHorasUsadas = []
                    for periodoProfesor in horariosUsado.periodos:
                        listaHorasUsadas.append(periodoProfesor.idHora)                    
                        if periodoProfesor.idperiodo == periodoProfesor:
                            #No se puede insertar en este periodo porque ya esta insertado en este
                            periodoEncontrado = 1
                            horarioFinal.agregarUnaAdvertencia(1,"No se logro asignar el profesor: " + self.nombre + " por que ya tiene asignado este periodo a esta hora: " + periodo.getHoraEnString(), 1)
                            return 0 #No se logro asignar el periodo

                    if periodo.idHora in listaHorasUsadas:
                        #No se puede insertar en este periodo porque ya tiene asignado un periodo en esta hora
                        periodoEncontrado = 1
                        horarioFinal.agregarUnaAdvertencia(1,"No se logro asignar el profesor: " + self.nombre + " por que ya tiene asignado un periodo a esta hora: " + periodo.getHoraEnString(), 1)
                        return 1 #No se logro asignar el periodo
        else: 
            return 1 # No se logro asignar el periodo porque no esta en horario laboral
        
        if horarioEncontrado == None:
            horarioInsertar = HorarioProfesor(horarioFinal)
            horarioInsertar.addPeriodo(periodo)
            self.horariosUsados.append(horarioInsertar)
            return 2 #Se asigno el periodo con el horario
        else:
            if periodoEncontrado == 0:
                horarioEncontrado.addPeriodo(periodo)
            return 3 #Se asigno el periodo el periodo
    
    # Si retorna en 1 es que si esta en hora 
    def calcularEstaDentroHoraDeContratacion(self,periodo,duracionPeriodo):
        #Hora inicial del periodo debe estar dentro de la hora inicial del profesor
        horaInicialProfesor = self.horarioContratacion.horaInicial
        horaFinalProfesor = self.horarioContratacion.horaFinal

        horaInicialPeriodo = periodo.horario.horaInicial.time()
        horaFinalPeriodo = periodo.horario.horaFinal.time()

        iniciaEnHora = 0
        terminaEnHora = 0
        if horaInicialProfesor <= horaInicialPeriodo:
            iniciaEnHora = 1
        if horaFinalProfesor >= horaFinalProfesor:
            terminaEnHora = 1
        
        if iniciaEnHora == 1 and terminaEnHora == 1:
            return 1
        #Hora final debe estar dentro de la hora del profesor
        print("Calcular horario de trabajo del profesor")



        
                
                    

                    

        
        

                    
        

                
        


            



        

