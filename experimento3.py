import datetime
from classes.controlDatos import ControlDatos

class MockData:
    def __init__(self):
        self.control1 = None
    
    def analizarDatos(self):
        control = ControlDatos()
        """Creacion de carreras: Codigo, Nombre"""
        control.setCarrera(1,"Ing. Ciencias y Sistemas")
        control.setCarrera(2,"Ing. Mecatronica")
        control.setCarrera(5,"Ing. Industrial")
    
    
        """Creacion de cursos  Codigo, Nombre, Creditos, Semestre, Duracion(horas la semana), Carrera, Cantidad de estudiantes"""
        control.setCurso(1011,"Curso 1", 5, 1, 3, 1, 10)
        control.setCurso(1012,"Curso 2", 5, 3, 3, 1, 10)
        control.setCurso(1013,"Curso 3", 5, 5, 3, 1, 10)
        control.setCurso(1014,"Curso 4", 5, 7, 3, 1, 10)
        control.setCurso(1015,"Curso 5", 5, 9, 3, 1, 10)
        control.setCurso(1016,"Curso 6", 5, 1, 3, 1, 10)
        control.setCurso(1017,"Curso 7", 5, 3, 3, 1, 10)
        control.setCurso(1018,"Curso 8", 5, 5, 3, 1, 10)
        control.setCurso(1019,"Curso 9", 5, 7, 3, 1, 10)
        control.setCurso(1020,"Curso 10", 5, 9, 3, 1, 10)
        control.setCurso(1021,"Curso 11", 5, 1, 3, 1, 10)
        control.setCurso(1022,"Curso 12", 5, 3, 3, 1, 10)
        control.setCurso(1023,"Curso 13", 5, 5, 3, 1, 10)
        control.setCurso(1024,"Curso 14", 5, 7, 3, 1, 10)
        control.setCurso(1025,"Curso 15", 5, 9, 3, 1, 10)
        control.setCurso(1026,"Curso 16", 5, 1, 3, 2, 10)
        control.setCurso(1027,"Curso 17", 5, 3, 3, 2, 10)
        control.setCurso(1028,"Curso 18", 5, 5, 3, 2, 10)
        control.setCurso(1029,"Curso 19", 5, 7, 3, 2, 10)
        control.setCurso(1030,"Curso 20", 5, 9, 3, 2, 10)
        control.setCurso(1031,"Curso 21", 5, 1, 3, 2, 10)
        control.setCurso(1032,"Curso 22", 5, 3, 3, 2, 10)
        control.setCurso(1033,"Curso 23", 5, 5, 3, 2, 10)
        control.setCurso(1034,"Curso 24", 5, 7, 3, 2, 10)
        control.setCurso(1035,"Curso 25", 5, 9, 3, 2, 10)
        control.setCurso(1036,"Curso 26", 5, 1, 3, 2, 10)
        control.setCurso(1037,"Curso 27", 5, 3, 3, 2, 10)
        control.setCurso(1038,"Curso 28", 5, 5, 3, 2, 10)
        control.setCurso(1039,"Curso 29", 5, 7, 3, 2, 10)
        control.setCurso(1040,"Curso 30", 5, 9, 3, 2, 10)
        control.setCurso(1041,"Curso 31", 5, 1, 3, 2, 10)
        control.setCurso(1042,"Curso 32", 5, 3, 3, 2, 10)
        control.setCurso(1043,"Curso 33", 5, 5, 3, 3, 10)
        control.setCurso(1044,"Curso 34", 5, 7, 3, 3, 10)
        control.setCurso(1045,"Curso 35", 5, 9, 3, 3, 10)
        control.setCurso(1046,"Curso 36", 5, 1, 3, 3, 10)
        control.setCurso(1047,"Curso 37", 5, 3, 3, 3, 10)
        control.setCurso(1048,"Curso 38", 5, 5, 3, 3, 10)
        control.setCurso(1049,"Curso 39", 5, 7, 3, 3, 10)
        control.setCurso(1050,"Curso 40", 5, 9, 3, 3, 10)
    
        """Creacion de salones: Codigo de Salon, Cantidad de Asientos"""
        control.setSalon(1,10)
        control.setSalon(2,10)
        control.setSalon(3,10)
        control.setSalon(4,10)
        control.setSalon(5,10)
        control.setSalon(6,10)       
    
        """Creacion de profesores: Nombre, Cursos que puede dar, horario de contratacion, carrera"""
        control.setProfesor("Dolore", [1011,1012,1013], [datetime.time(8,00,00), datetime.time(18,00,00)],1)
        control.setProfesor("Marial", [1014,1015,1016], [datetime.time(8,00,00), datetime.time(18,00,00)],1)
        control.setProfesor("Paulon", [1017,1018,1019], [datetime.time(8,00,00), datetime.time(18,00,00)],1)
        control.setProfesor("Wilson", [1020,1021,1022], [datetime.time(8,00,00), datetime.time(18,00,00)],1)
        control.setProfesor("Cinzia", [1023,1024,1025], [datetime.time(8,00,00), datetime.time(18,00,00)],1)
        control.setProfesor("Aguado", [1026,1027,1028], [datetime.time(8,00,00), datetime.time(18,00,00)],2)
        control.setProfesor("Bernad", [1029,1031,1032], [datetime.time(8,00,00), datetime.time(18,00,00)],2)
        control.setProfesor("Blasco", [1033,1034,1035], [datetime.time(8,00,00), datetime.time(18,00,00)],2)
        control.setProfesor("Boiras", [1036,1037,1038], [datetime.time(8,00,00), datetime.time(18,00,00)],2)
        control.setProfesor("Ariase", [1039,1040,1041], [datetime.time(8,00,00), datetime.time(18,00,00)],2)
        control.setProfesor("Alvaro", [1042,1043,1044], [datetime.time(8,00,00), datetime.time(18,00,00)],3)
        control.setProfesor("Santos", [1045,1046,1047], [datetime.time(8,00,00), datetime.time(18,00,00)],3)
        control.setProfesor("Mayrae", [1048,1049,1050], [datetime.time(8,00,00), datetime.time(18,00,00)],3)
        control.setProfesor("Guidor", [1042,1043,1044], [datetime.time(8,00,00), datetime.time(18,00,00)],3)
        control.setProfesor("Manuel", [1045,1046,1047], [datetime.time(8,00,00), datetime.time(18,00,00)],3)
        
        return control
    
    
    
    
    
    
    
    
    