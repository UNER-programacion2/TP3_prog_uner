from pizza import Pizza 
from pizzavariedad import PizzaVariedad  

class Mozo:
#####<<Atributos de instancia>>
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__pizzas = []  
#####<<Comandos>>
    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPizzas(self, pizzas: list[Pizza]):
        pizzasTomadas = len(self.__pizzas)
        pizzasATomar = len(pizzas)

       
        if pizzasTomadas + pizzasATomar > 2:
            print(self.__nombre + ": El mozo puede tomar un máximo de 2 pizzas!")
            return
        
        
        for pizza in pizzas:
            print(self.__nombre + ": tomando una Pizza de " + pizza.obtenerVariedad().obtenerNombreVariedad() + " para ser entregada")
            self.__pizzas.append(pizza)

    def servirPizzas(self):
        for pizza in self.__pizzas:
            print(self.__nombre + ": Sirviendo pizza de " + pizza.obtenerVariedad().obtenerNombreVariedad())
        self.__pizzas = []  

#####<<Consultas>>

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerPizzas(self):
        return self.__pizzas
    
    def obtenerEstadoLibre(self):
        if len(self.__pizzas) == 0: 
            return True
    
