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
        <p data-item='Horario_Generativo'>Horario Generativo</p>
        <div>Genera uno o varios horarios en base al archivo que se selecciono</div>                      
        <section class="pruebaSection">                       
            <nav>
                <div class="seccionCentrada">Tipo de generacion</div>
                <ul class="menuItems">            
                    <form action="/upload" method="post" enctype="multipart/form-data">
                        <input type="file" name="file">
                        <input type="submit" value="Upload">
                        <li><a href='#' data-item='Codigo_Ascendente'>Codigo_Ascendente</a></li>
                        <li><a href='#' data-item='Codigo_Descendente'>Codigo_Descendente</a></li>
                        <li><a href='#' data-item='Prioridad'>Prioridad</a></li>
                        <li><a href='#' data-item='Cantidad_Estudiantes'>Cantidad_Estudiantes</a></li> 
                    </form>         
                </ul>
            </nav>      
        </section>        	    
    </body>
</html>