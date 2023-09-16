import jsonpickle
import mysql.connector
import datetime
from classes.horariosMostrar import HorariosMostrar
from classes.guardadoHorarios import GuardadoHorarios

class ConexionDB:

    def __init__(self):
        print("SE realiza una conexion")
        
    
    def insertarHorarios(self,horarios):
        connection = mysql.connector.connect(
            host="localhost",
            user="adminHorarios",
            password="password123",
            database="base_Horarios"
        )
        #Se serealiza a json pa guardarse
        serializedHorario1 = jsonpickle.encode(horarios, unpicklable=True)
        print(serializedHorario1)
        cursor = connection.cursor()
        #insert_query = "INSERT INTO your_table (data) VALUES (%s)"
        insert_query = "INSERT INTO horario (fecha_hora, nombre, datos) VALUES (%s, %s, %s);"
        cursor.execute(insert_query, (self.getFechaActual(),horarios.nombre,serializedHorario1))
        connection.commit()
        cursor.close()
        connection.close()
        print("insertando")
    
    def traerTodosHorarios(self):
        horariosR = []

        connection = mysql.connector.connect(
            host="localhost",
            user="adminHorarios",
            password="password123",
            database="base_Horarios"
        )

        cursor = connection.cursor()

        select_query = "SELECT id_Horario, fecha_hora, nombre FROM horario"
        cursor.execute(select_query)
        
        resultados = cursor.fetchall()

        connection.close()

        for resultado in resultados:            
            id_Horario, fecha_hora, nombre = resultado
            horarioN = HorariosMostrar(id_Horario,fecha_hora,nombre)
            horariosR.append(horarioN)            

        return horariosR

    def traerHorarioPorCodigo(self,codigo):      
        horariosR = []

        connection = mysql.connector.connect(
            host="localhost",
            user="adminHorarios",
            password="password123",
            database="base_Horarios"
        )

        cursor = connection.cursor()

        select_query = "SELECT id_horario , datos FROM horario WHERE id_Horario = %s"
        cursor.execute(select_query, (codigo,))    
        
        resultado = cursor.fetchall()

        connection.close()
        datos = ""
        if resultado:
            idHorario, datos = resultado[0]            
        
        horarioGuardado = jsonpickle.decode(datos, classes=[GuardadoHorarios])  
        print(type(horarioGuardado))

        print(horarioGuardado.nombre)

        return horarioGuardado.horarios
        


    def getFechaActual(self):
        # Obtener la fecha y hora actual en un formato personalizado
        fecha_actual = datetime.datetime.now()
        formato_personalizado = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")

        # Imprimir la fecha y hora en formato personalizado
        return formato_personalizado  