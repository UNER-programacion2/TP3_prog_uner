class PizzaVariedad:
#####<<Atributos de instancia>>
    def __init__(self, nomvar: str, precio: float):
        self.__nombreVariedad = nomvar
        self.__precio = precio

#####<<Comandos>>
    def establecerNombreVariedad(self, nomVar: str):
        self.__nombreVariedad = nomVar

    def establecerPrecio(self, pre: float):
        if pre <= 0.0:
            print("Error: el precio es menor o igual a cero, reingrese nuevamente.")
        else:
            self.__precio = pre

#####<<Consultas>>
    def obtenerNombreVariedad(self):
        return self.__nombreVariedad

    def obtenerPrecio(self):
        return self.__precio 