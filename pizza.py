from pizzavariedad import PizzaVariedad

class Pizza:

    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3


    def __init__(self, var: PizzaVariedad):
        self.__variedad = var
        self.__estado = Pizza.ESTADO_POR_COCINAR

########comandos 
    def establecerVariedad(self, var: PizzaVariedad):
        self.__variedad = var
    
    def establecerEstado(self, est: int ):
        if est not in [Pizza.ESTADO_POR_COCINAR, Pizza.ESTADO_COCINADA, Pizza.ESTADO_ENTREGADA]:
            raise ValueError("Estado no válido.") 
        elif self.__estado == Pizza.ESTADO_POR_COCINAR:
            self.__estado = Pizza.ESTADO_COCINADA
        elif self.__estado == Pizza.ESTADO_COCINADA:
            self.__estado = Pizza.ESTADO_POR_COCINAR
        else:
             raise ValueError("No se puede hacer esa transición") 
         
      #consultas
    def obtenerVariedad(self):
        return self.__variedad

    def obtenerEstado(self):
        return self.__estado
    
    def __repr__(self):
        return self.__variedad






# <<Constructores>>
# Pizza(var: PizzaVariedad)
# Requiere var ligado
# <<Comandos>>
# establecerVariedad(var: PizzaVariedad)
# Requiere var ligado
# establecerEstado(est: int)
# <<Consultas>>
# obtenerVariedad(): PizzaVariedad
# obtenerEstado(): int