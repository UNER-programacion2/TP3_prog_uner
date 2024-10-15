from maestropizzero import MaestroPizzero
from mozo import Mozo
from orden import Orden
from pizzavariedad import PizzaVariedad
from pizza import Pizza


class TesterPizzeria:

    def main(self):
        muzza = PizzaVariedad("Muzzarella", 6500.00)
        fugazetta = PizzaVariedad("Fugazetta", 7560.50)
        napolitana = PizzaVariedad("Napolitana", 5700.00)
        rucula = PizzaVariedad("Rucula y Crudo", 4000.00)
        calabresa = PizzaVariedad("Calabresa", 8275.00)
        provolone = PizzaVariedad("Provolone", 8400.00)
        anana = PizzaVariedad("Anana", 5070.00)

        pizza1 = Pizza(muzza)
        pizza2 = Pizza(fugazetta)
        pizza3 = Pizza(napolitana)
        pizza4 = Pizza(rucula)
        pizza5 = Pizza(calabresa)
        pizza6 = Pizza(provolone)
        pizza7 = Pizza(anana)
        

        orden1 = Orden(1, [pizza1, pizza4])
        orden2 = Orden(2, [pizza2, pizza7])
        orden3 = Orden(3, [pizza3, pizza6, pizza5])
        ordenes = [orden1, orden2, orden3 ]
        
        pipo = MaestroPizzero("Pipo")
        augus = Mozo("Augusto")
        bea = Mozo("Beatriz")

        print('----------------------------------------\nPizzeria de Don Pipo\n----------------------------------------')

        print("\nTomando pedidos...")
        for orden in ordenes:
            print("Pipo tomando pedido #" + str(orden.obtenerNroOrden()))
            pipo.tomarPedido(orden)

        self.__imprimirEstado(pipo, augus, bea)
        
        print("\nCocinando pedidos...")
        pipo.cocinar()

        self.__imprimirEstado(pipo, augus, bea)
    #tomando pizzas
        augus.tomarPizzas(pipo.entregar(orden1))
        bea.tomarPizzas(pipo.entregar(orden2))
        
        self.__imprimirEstado(pipo, augus, bea)
    #sirviendo pizzas
        print("")
        augus.servirPizzas()
        bea.servirPizzas()
        
        self.__imprimirEstado(pipo, augus, bea)

        augus.tomarPizzas(pipo.entregar(orden3))
    
        
        self.__imprimirEstado(pipo, augus, bea)

        print("")
        augus.servirPizzas()
        bea.servirPizzas()
        
        self.__imprimirEstado(pipo, augus, bea)

        augus.tomarPizzas(pipo.entregar(orden3))
        
        self.__imprimirEstado(pipo, augus, bea)

        print("")
        augus.servirPizzas()
        
        self.__imprimirEstado(pipo, augus, bea)

        self.__totalOrd(ordenes)


    #calcular total de las ordenes
    def __totalOrd(self, ordenes : list[Orden]):
        for orden in ordenes:
            total_ord = orden.calcularTotal()
            print(f"Total de la orden {str(orden.obtenerNroOrden())}: {total_ord}" )

    
    def __imprimirEstado(self, maestroPizzero: MaestroPizzero, mozo1: Mozo, mozo2: Mozo):
        print("\nMaestro Pizzero: " + maestroPizzero.obtenerNombre() + "\n==============================")
        for orden in maestroPizzero.obtenerOrdenes():
            print(orden)
        print("==============================\nMozo: " + mozo1.obtenerNombre() + "\n==============================")
        for pizza in mozo1.obtenerPizzas():
            print(pizza)
        print("==============================\nMozo: " + mozo2.obtenerNombre() + "\n==============================")
        for pizza in mozo2.obtenerPizzas():
            print(pizza)

    # total = Orden.calcularTotal()
    # print(f"Costo total de la orden: ${total:.2f}")

if __name__ == "__main__":
    testerPizzeria = TesterPizzeria()
    testerPizzeria.main()
