class Mozo:

    def __init__(self, nom: str):
        self.__nombre = nom
        self.__pizzas = []

    def establecerNombre(self, nom: str):
        self.__nombre = nom

    def tomarPizzas(self, pizzas):
        pizzasTomadas = len(self.__pizzas)
        pizzasATomar = len(pizzas)
        if (pizzasATomar - pizzasTomadas) < 0:
            print(self.__nombre + ": El mozo puede tomar un máximo de 2 pizzas!")
        else:
            for pizza in pizzas:
                print(self.__nombre + ": tomando una de " + pizza.obtenerVariedad() + " para ser entregada")
                self.__pizzas.append(pizza)
    
    def servirPizzas(self):
        for pizza in self.__pizzas:
            print(self.__nombre + ": Sirviendo pizza de " + pizza.obtenerVariedad())
        self.__pizzas = []

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerPizzas(self):
        return self.__pizzas
    
    def obtenerEstadoLibre(self):
        pizzasTomadas = len(self.__pizzas)
        return pizzasTomadas < 2