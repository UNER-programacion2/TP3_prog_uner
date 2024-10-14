from pizzavariedad import PizzaVariedad  

class Pizza:
#####<<Atributos de clase>>
    ESTADO_POR_COCINAR = 1
    ESTADO_COCINADA = 2
    ESTADO_ENTREGADA = 3

#####<<Atributos de instancia>>
    def __init__(self, var: PizzaVariedad):
        self.__variedad = var
        self.__estado = Pizza.ESTADO_POR_COCINAR  

#####<<Comandos>>
    def establecerVariedad(self, var: PizzaVariedad):
        self.__variedad = var
    
    def establecerEstado(self, est: int):
        if est not in [Pizza.ESTADO_POR_COCINAR, Pizza.ESTADO_COCINADA, Pizza.ESTADO_ENTREGADA]:
            raise ValueError("Estado no válido.")
        
       
        if self.__estado == Pizza.ESTADO_POR_COCINAR and est == Pizza.ESTADO_COCINADA:
            self.__estado = Pizza.ESTADO_COCINADA
        elif self.__estado == Pizza.ESTADO_COCINADA and est == Pizza.ESTADO_ENTREGADA:
            self.__estado = Pizza.ESTADO_ENTREGADA
        else:
            raise ValueError("No se puede hacer esa transición")

#####<<Consultas>>
    def obtenerVariedad(self):
        return self.__variedad

    def obtenerEstado(self):
        return self.__estado
    
    # def __repr__(self):
    #     return f"{self.__variedad.obtenerNombreVariedad()} (Estado: {self.__estado})"
    def __str__(self):
        return f"Pizza de {self.__variedad} - Estado: {self.__estado}"
