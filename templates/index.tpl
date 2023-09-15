<!DOCTYPE html>
<html lang="en-US">
   <head>
      <meta charset="UTF-8">      
      <title>Horario</title>
      
      <link rel="stylesheet" href="scheduleStyle.css">   
      <link rel="stylesheet" href="mainStyle.css">
      <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600" rel="stylesheet">  
      <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js" type="text/javascript"></script>
      <script type = "text/javascript" src="transition.js"></script> 
   </head>   
   <body>                     
      <section class="pruebaSection">
         <br>            
         <nav>
         <div class="seccionCentrada">Tipo de generacion</div>
            <ul class="menuItems">          
               <li><a href='#' data-item='Codigo_Ascendente'>Codigo_Ascendente</a></li>
               <li><a href='#' data-item='Codigo_Descendente'>Codigo_Descendente</a></li>
               <li><a href='#' data-item='Prioridad'>Prioridad</a></li>
               <li><a href='#' data-item='Cantidad_Estudiantes'>Cantidad_Estudiantes</a></li>            
            </ul>
         </nav>      
      </section>      
      <p data-item='Horario_Generativo'>Horario Generativo</p>
      
      <div>Genera uno o varios horarios en base al archivo que se selecciono</div>   	
	  <div class="scrollable-div">		
		<table class="scrollable-table">
			<thead>
				<tr>
				    <th class="fixed-column"><h1></h1></th>
    	            % for salon in control.salones:
    	            <th><h1>{{salon.numero}}</h1></th>
    	            % end										
				</tr>
			</thead>
			<tbody>
    	        % vecesAgregado = 0
    	        % cantidadSalones = len(control.salones)
    	        % for p1 in cantPeriodos:
				<tr>
					<td class="fixed-column">{{p1}}</td>
    	            % for i in range(cantidadSalones):
    	                % periodoDibujar = horario.listaPeriodos[i+vecesAgregado]
    	                % if periodoDibujar.curso == None:
    	                    <td class="color1">{{periodoDibujar.idperiodo}}</td>
    	                % else:
    	                    <td class="color1">{{periodoDibujar.curso.nombre +" \n "+ periodoDibujar.profesor.nombre}}</td>					
    	                % end
    	            % end
    	            % vecesAgregado += cantidadSalones
				</tr>
				% end
			</tbody>
		</table>
      </div>	  
	  <section class="pruebaSection">
         <br>            
         <nav>
         <div class="seccionCentrada">Generacion de Advertencias</div>
            <ul class="menuItems">          
               <button onclick="mostrarTabla()">Mostrar Tabla</button>
            </ul>
         </nav>      
      </section>  
	  
    <table id="miTabla" border="1">
        <tr>
            <th>Encabezado 1</th>
            <th>Encabezado 2</th>
            <th>Encabezado 3</th>
        </tr>
        <tr>
            <td>Dato 1</td>
            <td>Dato 2</td>
            <td>Dato 3</td>
        </tr>
        <!-- Agrega más filas según sea necesario -->
    </table>
	<script>
        function mostrarTabla() {
            var tabla = document.getElementById("miTabla");
            if (tabla.style.display === "none") {
                tabla.style.display = "table"; // Muestra la tabla
            } else {
                tabla.style.display = "none"; // Oculta la tabla
            }
        }
    </script>
   </body>
</html>