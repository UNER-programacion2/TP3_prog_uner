# PizzaVariedad
# <<Atributos de clase>>
# <<Atributos de instancia>>
# nombreVariedad: string
# precio: float
# <<Constructores>>
# PizzaVariedad(nomVar: string, pre: float)
# Requiere pre > 0.0
# <<Comandos>>s
# establecerNombreVariedad(nomVar: string)
# establecerPrecio(pre: float)
# Requiere pre > 0.0
# <<Consultas>>
# obtenerNombreVariedad(): string
# obtenerPrecio(): float

class PizzaVariedad:

    def __init__(self, nombreVariedad: str, precio: float):
        self.__nombreVariedad = nombreVariedad
        self.__precio = precio    


    # def PizzaVariedad(self, nomVar: str , pre: float):
    #     self.__nombreVariedad = nomVar
    #     self.__precio = pre

        
            
    # comandos
    def establecerNombreVariedad(self, nomVariedad: str):
        self.nomVariedad = nomVariedad

    def establecerPrecio(self, precio: float):
        self.precio = precio

        if precio <= 0.0:
            print("Error el precio es menor a cero, reingrse nuevamente :I")



    # consultas

    def obtenerNombreVariedad(self):
        return self.__nomVariedad

    def obtenerPrecio(self):
        return self.__precio
    