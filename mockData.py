import datetime
from classes.controlDatos import ControlDatos

class MockData:
    def __init__(self):
        self.control1 = None
    
    def analizarDatos(self):
        control = ControlDatos()
        """Creacion de carreras: Codigo, Nombre"""
        control.setCarrera(1,"Ing. Ciencias y Sistemas")
        control.setCarrera(2,"Ing. Civil")
    
    
        """Creacion de cursos  Codigo, Nombre, Creditos, Semestre, Duracion(horas la semana), Carrera, Cantidad de estudiantes"""
        control.setCurso(1011,"Matematica Basica 2", 5, 2, 3, 2, 10)
        control.setCurso(1010,"Matematica Basica 1", 5, 1, 3, 1, 10)
        control.setCurso(1012,"Curso 1", 5, 1, 3, 1, 10)
        control.setCurso(1013,"Curso 2", 5, 3, 3, 1, 10)
        control.setCurso(1014,"Curso 3", 5, 1, 3, 1, 10)
        control.setCurso(1015,"Curso 4", 5, 1, 3, 2, 10)
        control.setCurso(1016,"Curso 5", 5, 2, 3, 1, 10)
    
        """Darle prioridad a ciertos cursos, si estos no se les agrega se pondra por defult una prioridad de 0"""
        control.setPrioridadCurso(1010,10)
        control.setPrioridadCurso(1011,9)
    
        """Creacion de salones: Codigo de Salon, Cantidad de Asientos"""
        control.setSalon(1,10)
        control.setSalon(2,10)
        control.setSalon(3,10)
        control.setSalon(4,10)
    
        """Creacion de estudiantes"""
        #Ya no se crean estudiantes porque se asignaran automaticamente
        #Los estudiantes seran asignados en los cursos al crear el curso
        #control.setEstudiante("Juan", [1010], [1011])
    
        """Creacion de profesores: Nombre, Cursos que puede dar, horario de contratacion, carrera"""
        control.setProfesor("Peter", [1011,1012,1013,1014,1015], [datetime.time(8,00,00), datetime.time(18,00,00)],1)
        control.setProfesor("Saul", [1012,1013], [datetime.time(8,00,00), datetime.time(18,00,00)],2)

        """Agregar algun profesor especifico a los cursos si es necesario"""
        control.setProfesorFijoACurso("Saul",1012)

        print("Datos ingresados correctamente")
        return control
    
    
    
    
    
    
    
    
    