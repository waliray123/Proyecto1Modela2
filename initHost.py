from bottle import route, get, run, template, static_file, redirect
from init import horariosRetornados, control, listaPeriodos


indiceActual = 0 

@route('/hello')
def hello():
    return template('templates/index.tpl',horario=horariosRetornados[indiceActual],control=control,cantPeriodos=listaPeriodos)

@route('/prueba')
def prueba():   
    global indiceActual 
    return template('templates/prueba.tpl',horario=horariosRetornados[indiceActual],control=control,cantPeriodos=listaPeriodos)

@route('/siguiente')
def siguiente():
    global indiceActual
    if indiceActual < len(horariosRetornados) - 1:
        indiceActual += 1
    return redirect('/prueba')

@route('/atras')
def atras():
    global indiceActual
    if indiceActual > 0:
        indiceActual -= 1
    return redirect('/prueba')


@get('/<filename:re:.*\.css>')
def stylesheets(filename):  
    return static_file(filename, root='static/css/')

@get('/<filename:re:.*\.js>')
def stylesheets(filename):
    return static_file(filename, root='static/js/')

run(host='localhost', port=8080, debug=True)