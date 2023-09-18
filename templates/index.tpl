<!DOCTYPE html>
<html lang="en-US">
    <head>
      <meta charset="UTF-8">      
      <title>Horario</title>
      
      <link rel="stylesheet" href="scheduleStyle.css">   
      <link rel="stylesheet" href="mainStyle.css">
      <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600" rel="stylesheet">  
      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
    </head>   
    <body>                        
        <p data-item='Horario_Generativo'>Horario Generativo</p>
        <div>Genera uno o varios horarios en base al archivo que se selecciono</div>                      
        <section class="pruebaSection">                       
            <nav>
                <div class="seccionCentrada">Tipo de generacion</div>
                <ul class="menuItems">            
                    <form action="/upload" method="post" enctype="multipart/form-data">
                        <li>
                            <label><input type="radio" id="Ascendente" name="tipo" value="Ascendente">                            
                            <a data-item='Codigo_Ascendente'>Codigo_Ascendente</a></label>
                        </li>
                        <li>
                            <label><input type="radio" id="Descendente" name="tipo" value="Descendente">
                            <a data-item='Codigo_Descendente'>Codigo_Descendente</a></label>
                        </li>
                        <li>
                            <label><input type="radio" id="Prioridad" name="tipo" value="Prioridad">
                            <a data-item='Prioridad'>Prioridad</a></label>
                        </li>
                        <li>
                            <label><input type="radio" id="Cantidad" name="tipo" value="Cantidad">
                            <a data-item='Cantidad_Estudiantes'>Cantidad_Estudiantes</a></label>
                        </li>
                        <br>
                        <label for="HoraInicial">Ingrese la hora inicial con el formato HH:MM AM/PM:</label>
                        <input type="text" id="HoraInicial" name="HoraInicial" >
                        <br>
                        <br>
                        <label for="HoraFinal">Ingrese la hora final con el formato HH:MM AM/PM:</label>
                        <input type="text" id="HoraFinal" name="HoraFinal">
                        <br>
                        <br>
                        <label for="Semestre">Ingrese el semestre a generar PAR/IMPAR:</label>
                        <input type="text" id="Semestre" name="Semestre">
                        <br>
                        <br>
                        <label for="Duracion">Ingrese la cantidad en minutos de la duracion del periodo:</label>
                        <input type="number" id="Duracion" name="Duracion" min="0" value="60">
                        <br>
                        <div id="cantidadPrioridadTextBox" style="display: none;">
                            <label for="cantidadPrioridad">Ingrese un valor numérico:</label>
                            <input type="number" id="cantidadPrioridad" name="cantidadPrioridad" min="0">
                        </div>
                        <br>
                        <input class="button" type="file" name="file">
                        <input class="button" type="submit" value="GENERAR">                        
                    </form>         
                </ul>
            </nav>      
        </section>      
        <section class="pruebaSection">                       
            <nav>
                <div class="seccionCentrada">Visualizacion de Horarios Creados Anteriormente</div>
                <ul class="menuItems">            
                    <li>                                                
                        <a href="/mostrarHistorico" data-item='Mostrar_Historico'>Mostrar_Historico</a>
                    </li>  
                </ul>
            </nav>      
        </section>    	    
        <script type = "text/javascript" src="transition.js"></script> 
        <script>
            // Obtener los elementos relevantes
            const cantidadPrioridadTextBox = document.getElementById('cantidadPrioridadTextBox');
            const cantidadPrioridadInput = document.getElementById('cantidadPrioridad');
            const cantidadRadio = document.getElementById('Cantidad');
            const prioridadRadio = document.getElementById('Prioridad');
            const codigoAscendenteRadio = document.getElementById('Ascendente');
            const codigoDescendenteRadio = document.getElementById('Descendente');


            // Función para mostrar u ocultar el textbox
            function toggleCantidadPrioridadTextBox() {
                if (cantidadRadio.checked || prioridadRadio.checked) {
                    cantidadPrioridadTextBox.style.display = 'block';
                } else {
                    cantidadPrioridadTextBox.style.display = 'none';
                    cantidadPrioridadInput.value = ''; // Borrar el valor cuando se oculta
                }
            }

            // Escuchar los eventos de cambio en los radios relevantes
            cantidadRadio.addEventListener('change', toggleCantidadPrioridadTextBox);
            prioridadRadio.addEventListener('change', toggleCantidadPrioridadTextBox);
            codigoAscendenteRadio.addEventListener('change', () => {
                cantidadPrioridadTextBox.style.display = 'none';
                cantidadPrioridadInput.value = ''; // Borrar el valor cuando se oculta
            });
            codigoDescendenteRadio.addEventListener('change', () => {
                cantidadPrioridadTextBox.style.display = 'none';
                cantidadPrioridadInput.value = ''; // Borrar el valor cuando se oculta
            });
            // Llamada inicial para asegurarse de que el estado esté sincronizado
            toggleCantidadPrioridadTextBox();
        </script>

    </body>
</html>