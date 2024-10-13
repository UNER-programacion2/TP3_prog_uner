class PizzaVariedad:

    def __init__(self, nomvar: str, precio: float):
        self.__nombreVariedad = nomvar
        self.__precio = precio    

#####comandos
    def establecerNombreVariedad(self, nomVar: str):
        self.nomVariedad = nomVar

    def establecerPrecio(self, pre: float):
        self.precio = pre

        if pre <= 0.0:
            print("Error el precio es menor a cero, reingrese nuevamente: ")

######consultas

    def obtenerNombreVariedad(self):
        return self.__nombreVariedad

    def obtenerPrecio(self):
        return self.__precio
    