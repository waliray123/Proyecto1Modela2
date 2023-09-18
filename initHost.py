from bottle import route, get, run, template, static_file, redirect, request
from connection.conexionDB import ConexionDB
from classes.guardadoHorarios import GuardadoHorarios
from init import Inicializador
import os

conexion = ConexionDB()
esNuevo = 0
codigoHorarioVer = 0
indiceActual = 0 
esPrimero = 1
horariosR = []
tipoGeneracion = ""
cantidadCorridas = ""
control = None
cantPeriodos = None
duracionPeriodo = 50
semestreUsar = 0
strHoraI = "7:00 AM"
strHoraF = "1:00 PM"

@route('/')
def index():
    global esPrimero, esNuevo
    esPrimero = 1
    esNuevo = 0
    return template('templates/index.tpl')

@route('/prueba')
def prueba():   
    global indiceActual,horariosR,esPrimero,conexion,codigoHorarioVer,esNuevo,tipoGeneracion,cantidadCorridas,control,cantPeriodos,duracionPeriodo,semestreUsar,strHoraI,strHoraF
    if esNuevo == 0:
        if esPrimero == 1:            
            iniciar = Inicializador(tipoGeneracion,cantidadCorridas,duracionPeriodo,semestreUsar,strHoraI,strHoraF)
            indiceActual = 0
            horariosR = iniciar.horariosRetornados
            control = iniciar.control1
            cantPeriodos = iniciar.listaPeriodos
            horarioAGuardar = GuardadoHorarios(horariosR,"Es una prueba de nombre")
            conexion.insertarHorarios(horarioAGuardar)
    else:
        indiceActual = 0
        horariosR = conexion.traerHorarioPorCodigo(codigoHorarioVer)
        print("obtenido")
    
    return template('templates/prueba.tpl',horario=horariosR[indiceActual],indice=indiceActual)

@route('/mostrarHistorico')
def mostrarHistorico():   
    global conexion
    horariosR = conexion.traerTodosHorarios()
    return template('templates/mostrarHistorico.tpl',horariosR=horariosR)

@route('/redireccion/<valor>')
def redireccion(valor):   
    global codigoHorarioVer, esNuevo    
    codigoHorarioVer = valor   
    esNuevo = 1
    return redirect('/prueba')

@route('/siguiente')
def siguiente():
    global indiceActual,esPrimero,horariosR
    esPrimero = 0
    if indiceActual < len(horariosR) - 1:
        indiceActual += 1
    return redirect('/prueba')

@route('/atras')
def atras():
    global indiceActual,esPrimero,horariosR
    esPrimero = 0
    if indiceActual > 0:
        indiceActual -= 1
    return redirect('/prueba')

@route('/prueba2')
def prueba2():       
    return template('templates/prueba2.tpl')

@route('/upload', method='POST')
def do_upload():
    global tipoGeneracion, cantidadCorridas,duracionPeriodo,semestreUsar,strHoraI,strHoraF
    tipoGeneracion = request.forms.get('tipo')
    cantidadCorridas = request.forms.get('cantidadPrioridad')
    duracionPeriodo = request.forms.get('Duracion')
    semestreUsar = request.forms.get('Semestre')
    strHoraI = request.forms.get('HoraInicial')
    strHoraF = request.forms.get('HoraFinal')

    if duracionPeriodo == '':
        duracionPeriodo = 50
    
    if semestreUsar == '':
        semestreUsar = 0
    
    if strHoraI == '':
        strHoraI = "7:00 AM"
    
    if strHoraF == '':
        strHoraF = "1:00 PM"




    
    """
    if cantidadCorridas == "":
        print("None")
    else:
        print(cantidadCorridas)
    """

    uploaded_file = request.files.get('file')

    if uploaded_file:
        save_path = "datos/"  # Specify the path where you want to save uploads
        custom_file_name = "mockD.py"  # Specify the desired file name

        file_path = os.path.join(save_path, custom_file_name)

        # Remove the existing file if it exists
        if os.path.exists(file_path):
            os.remove(file_path)

        # Save the uploaded file with the specified name
        uploaded_file.save(file_path)

        return redirect('/prueba')
    else:
        return redirect('/')


@get('/<filename:re:.*\.css>')
def stylesheets(filename):  
    return static_file(filename, root='static/css/')

@get('/<filename:re:.*\.js>')
def stylesheets(filename):
    return static_file(filename, root='static/js/')

run(host='localhost', port=8080, debug=True)