<!DOCTYPE html>
<html>
<head>
    <title>Lista de Elementos</title>
</head>
<body>
    {{horario.nombre}}

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
</body>
</html>