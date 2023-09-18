import datetime
from classes.controlDatos import ControlDatos

class MockData:
    def __init__(self):
        self.control1 = None
    
    def analizarDatos(self):
        control = ControlDatos()
        """Creacion de carreras: Codigo, Nombre"""
        control.setCarrera(1,"Ing. Ciencias y Sistemas")
    
    
        """Creacion de cursos  Codigo, Nombre, Creditos, Semestre, Duracion(horas la semana), Carrera, Cantidad de estudiantes"""
        control.setCurso(1011,"Curso 1", 5, 1, 3, 1, 10)
        control.setCurso(1012,"Curso 2", 5, 3, 3, 1, 10)
        control.setCurso(1013,"Curso 3", 5, 5, 3, 1, 10)
        control.setCurso(1014,"Curso 4", 5, 3, 3, 1, 10)
        control.setCurso(1015,"Curso 5", 5, 1, 3, 1, 10)
    
        """Creacion de salones: Codigo de Salon, Cantidad de Asientos"""
        control.setSalon(1,10)
    
        """Creacion de profesores: Nombre, Cursos que puede dar, horario de contratacion, carrera"""
        control.setProfesor("Peter", [1011,1012,1013,1014,1015], [datetime.time(8,00,00), datetime.time(18,00,00)],1)
        
        return control
    
    
    
    
    
    
    
    
    