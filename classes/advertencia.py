class Advertencia:
    #Estas advertencias son las que apareceran, si se escoge hacerlo, y avisaran sobre acciones que se realizaron
    #Habran varios tipos de advertencias: [1]Normal, [2]Grave, [3]Irreparable 
    #Si es una advertencia Normal es muy probable que se pueda arreglar con el paso del tiempo, o en otras iteraciones que esten por realizarse
    #Se es una advertencia grave, quiere decir que una accion que se suponia que tenia que suceder no sucedio pero podria tener arreglo
    #Si es tiene una advertencia de tipo irreparable, entonces nos indica que el codigo no puede llegar a resolver el problema

    #Las advertencias pueden suceder en varias secciones: [1]Asignacion de profesor, [2]asignacion de curso, [3]asignacion de periodo    
    def __init__(self,tipo,contenido,tipoAsignacion):
        self.tipo = tipo
        self.contenido = contenido
        self.asignacion = tipoAsignacion

