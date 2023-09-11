from datetime import datetime, timedelta

def calcular_periodos(inicio, fin, duracion_periodo):
    # Convertir las horas iniciales y finales a minutos
    inicio_minutos = (inicio.hour * 60) + inicio.minute
    fin_minutos = (fin.hour * 60) + fin.minute
    
    # Calcular la duración total en minutos
    duracion_total = fin_minutos - inicio_minutos
    
    # Calcular la cantidad de periodos completos
    periodos_completos = duracion_total // duracion_periodo
    
    # Generar la lista de periodos con sus respectivas divisiones de tiempo
    periodos_lista = []
    for i in range(periodos_completos):
        periodo_inicio = inicio + timedelta(minutes=i * duracion_periodo)
        periodo_fin = inicio + timedelta(minutes=(i + 1) * duracion_periodo)
        periodos_lista.append((periodo_inicio.strftime("%I:%M %p"), periodo_fin.strftime("%I:%M %p")))
    
    return periodos_lista

# Ejemplo de uso
inicio = datetime.strptime("8:00 AM", "%I:%M %p")
fin = datetime.strptime("1:00 PM", "%I:%M %p")
duracion_periodo = 50

periodos = calcular_periodos(inicio, fin, duracion_periodo)
print(periodos)

for i, periodo in enumerate(periodos, 1):
    print(f"Periodo {i}: {periodo[0]} - {periodo[1]}")