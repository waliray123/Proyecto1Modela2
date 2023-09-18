<!DOCTYPE html>
<html>
<head>
    <title>Lista de Elementos</title>
    <link rel="stylesheet" href="tablaHorario.css">
</head>
<body>
    <div class="container">
        <h1 class="titulo">{{horario.nombre}}</h1>
        <h2 class="subtitulo">Numero de Horario Generado: {{indice}}</h2>
        <p class="parrafo">Eficiencia de Cursos Asignados: {{horario.eficicienciaCursosAsignados}}</p>
        <p class="parrafo">Eficiencia de Usabilidad de periodos: {{horario.eficienciaUsabilidadPeriodos}}</p>
        <a href="/atras" data-item='Anterior_Horario'>Anterior_Horario</a>
        <a href="/siguiente" data-item='Siguiente_Horario'>Siguiente_Horario</a>
    </div>
    <div class="table-container">
        <div class="table-scroll">
            <table class="scrollable">
	        	<thead>
	        		<tr>
	        		    <th class="fixed-column"><h1></h1></th>
                        % for salon in horario.salones:
                        <th><h1>{{salon.numero}}</h1> <br>Asientos:{{salon.asientos}}</th>
                        % end										
	        		</tr>
	        	</thead>
	        	<tbody>
                    % vecesAgregado = 0
                    % cantidadSalones = len(horario.salones)
                    % for p1 in horario.cantidadPeriodos:
	        		<tr>
	        			<td class="fixed-column">{{p1}}</td>
                        % for i in range(cantidadSalones):
                            % periodoDibujar = horario.listaPeriodos[i+vecesAgregado]
                            % if periodoDibujar.curso == None:
                                <td class="color1"></td>
                            % else:
                                <td style="background-color: {{periodoDibujar.curso.color}};"> 
                                    {{periodoDibujar.curso.codigo}}
                                    <br>
                                    {{periodoDibujar.curso.nombre}}
                                    <br>
                                    {{periodoDibujar.profesor.nombre}} 
                                    <br>
                                    Alumnos: {{periodoDibujar.curso.cantidadEstudiantes}} 
                                    Semestre: {{periodoDibujar.curso.semestre}} 
                                </td>                                			
                            % end
                        % end
                        % vecesAgregado += cantidadSalones
	        		</tr>
	        		% end
	        	</tbody>
	        </table>
        </div>
    </div>
    <div class="container">        
        <h2 class="subtitulo">Advertencias de la creacion del horario</h2>        
    </div>
        <div class="table-scroll">
            <table class="scrollable">
	        	<thead>
	        		<tr>
	        		    <th class="fixed-column"><h1>Tipo de Advertencia</h1></th>
	        		    <th class="fixed-column"><h1>Tipo de Asignacion</h1></th>
	        		    <th class="fixed-column"><h1>Tipo de Contenido</h1></th>
	        		</tr>
	        	</thead>
	        	<tbody>	        		        			
                        % for advertencia in horario.advertencias:
                            <tr>
                            <td class="fixed-column">
                            % if advertencia.tipo == 1:
                                Normal
                            % elif advertencia.tipo == 2:
                                Grave
                            % elif advertencia.tipo == 3:
                                Irreparable
                            % end
                            </td>
                            <td class="fixed-column">{{advertencia.asignacion}}</td>
                            <td class="fixed-column">{{advertencia.contenido}}</td>
                            </tr>
                        % end	        		
	        	</tbody>
	        </table>
        </div>    
</body>
</html>