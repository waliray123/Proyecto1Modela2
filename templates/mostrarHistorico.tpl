<!DOCTYPE html>
<html>
<head>
    <title>Lista de Elementos</title>
</head>
<body>    
    <table class="scrollable-table">
		<thead>
			<tr>
			    <th class="fixed-column"><h1>ID Horario</h1></th>
                <th class="fixed-column"><h1>Fecha Creacion</h1></th>
                <th class="fixed-column"><h1>Nombre</h1></th>
                <th class="fixed-column"><h1>Visualizacion</h1></th>
			</tr>
		</thead>
		<tbody>
            % for h1 in horariosR:
			<tr>
				<td class="fixed-column">{{h1.idHorario}}</td>
				<td class="fixed-column">{{h1.fecha}}</td>
				<td class="fixed-column">{{h1.nombre}}</td>
				<td class="fixed-column"><a href="/redireccion/{{ h1.idHorario }}">Redirigir</a></td>
			</tr>
			% end
		</tbody>
	</table>
</body>
</html>