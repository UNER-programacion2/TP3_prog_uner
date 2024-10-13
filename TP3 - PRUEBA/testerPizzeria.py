from pizzavariedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo

########################################################Este funcionaba######################################################
# class TesterPizzeria:
#     def main(self):
#         # Crear objetos
#         maestro = MaestroPizzero("Marcos")
#         mozo1 = Mozo("Juan")
#         mozo2 = Mozo("Pedro")

#         variedad1 = PizzaVariedad("Muzzarella", 500) 
#         variedad2 = PizzaVariedad("Napolitana", 540)
        
#         pizza1 = Pizza(variedad1)
#         pizza2 = Pizza(variedad2)
        
#         orden1 = Orden(1, [pizza1, pizza2])
        
#         # Procesar pedidos
#         maestro.tomarPedido(orden1)
#         maestro.cocinar()
#         pizzas_entregadas = maestro.entregar(orden1)
        
#         mozo1.tomarPizzas(pizzas_entregadas)
#         mozo1.servirPizzas()
        
#         # Mostrar estados y costos
#         print(f"Número de Orden: {orden1.obtenerNroOrden()}")
#         print(f"Pizzas en la Orden: {[pizza.obtenerVariedad() for pizza in orden1.obtenerPizzas()]}")
#         print(f"Estado de la orden: {orden1.obtenerEstadoOrden()}")
#         print(f"Costo total de la orden: {orden1.calcularTotal()}")

# if __name__ == '__main__':
#     tester_pizzeria = TesterPizzeria()
#     tester_pizzeria.main()



#a.Crear objetos de tipo PizzaVariedad, Pizza, Orden, MaestroPizzero y Mozo.
#b. Enviar los mensajes tomarPedido, cocinar y entregar al objeto de la clase
#MaestroPizzero.
#c. Enviar los mensajes tomarPizzas y servirPizzas a los objetos de la clase Mozo
#creados en el punto a.
#d. Mostrar la transición de estados de los objetos de las clases Orden y Pizza.
#e. Calcular y mostrar el costo total de las órdenes creadas.






#############################################################################################################
class TesterPizzeria:
    def main(self):
        # Crear objetos
        variedad_muzzarella = PizzaVariedad("Muzzarella", 500)
        variedad_napolitana = PizzaVariedad("Napolitana", 600)
        
        pizza1 = Pizza(variedad_muzzarella)
        pizza2 = Pizza(variedad_napolitana)
        
        orden1 = Orden(1, [pizza1, pizza2])
        
        maestro = MaestroPizzero("Pedro")
        mozo1 = Mozo("Juan")
        mozo2 = Mozo("Pedro")
        
        # Procesar pedidos
        maestro.tomarPedido(orden1)
        maestro.cocinar()
        pizzas_entregadas = maestro.entregar(orden1)
        
        mozo1.tomarPizzas(pizzas_entregadas)
        mozo1.servirPizzas()

        mozo2.tomarPizzas(pizzas_entregadas)
        mozo2.servirPizzas()
        
        # Mostrar estados y costos
        print(f"Estado de la orden: {orden1.obtenerEstadoOrden()}")
        print(f"Costo total de la orden: {orden1.calcularTotal()}")

if __name__ == '__main__':
    tester_pizzeria = TesterPizzeria()
    tester_pizzeria.main()



############################################################################################################
# gabi 
# class TesterPizzeria:
#     def main(self):
#         # 7.a: Crear objetos de tipo PizzaVariedad, Pizza, Orden, MaestroPizzero y Mozo.
#         variedad1 = PizzaVariedad("Margarita", 300)
#         variedad2 = PizzaVariedad("Pepperoni", 500)
        
#         pizza1 = Pizza(variedad1)
#         pizza2 = Pizza(variedad2)

#         orden1 = Orden(1, [pizza1, pizza2])

#         maestro_pizzero = MaestroPizzero("Carlos")
#         mozo = Mozo("Ana")

#         # 7.b: Enviar los mensajes tomarPedido, cocinar y entregar al objeto de la clase MaestroPizzero.
#         print("Tomando pedido...")
#         maestro_pizzero.tomarPedido(orden1)

#         print("Cocinando...")
#         maestro_pizzero.cocinar()

#         print("Estado de las pizzas después de cocinar:")
#         for pizza in orden1.obtenerPizzas():
#             print(f"Pizza: {pizza.variedad.obtenerNombreVariedad()}, Estado: {pizza.obtenerEstado()}")

#         print("Entregando pizzas...")
#         pizzas_entregadas = maestro_pizzero.entregar(orden1)

#         print("Estado de las pizzas después de entregar:")
#         for pizza in pizzas_entregadas:
#             print(f"Pizza: {pizza.variedad.obtenerNombreVariedad()}, Estado: {pizza.obtenerEstado()}")

#         # 7.c: Enviar los mensajes tomarPizzas y servirPizzas a los objetos de la clase Mozo.
#         print("Tomando pizzas por el mozo...")
#         mozo.tomarPizzas(pizzas_entregadas)

#         print("Sirviendo pizzas...")
#         mozo.servirPizzas()

#         # 7.d: Mostrar la transición de estados de los objetos de las clases Orden y Pizza.
#         print(f"Estado de la orden: {orden1.obtenerEstadoOrden()}")

#         # 7.e: Calcular y mostrar el costo total de las órdenes creadas.
#         total = orden1.calcularTotal()
#         print(f"Costo total de la orden: ${total:.2f}")



# if __name__ == '__main__':
#     testerPizzeria = TesterPizzeria()
#     testerPizzeria.main()
