from pizzavariedad import PizzaVariedad
from pizza import Pizza
from orden import Orden
from maestropizzero import MaestroPizzero
from mozo import Mozo

import os
# class TesterPizzeria:
#     def main(self):
#         # Crear objetos
#         variedad_muzzarella = PizzaVariedad("Muzzarella", 500)
#         variedad_napolitana = PizzaVariedad("Napolitana", 600)
        
#         pizza1 = Pizza(variedad_muzzarella)
#         pizza2 = Pizza(variedad_napolitana)
        
#         orden1 = Orden(1, [pizza1, pizza2])
        
#         maestro = MaestroPizzero("Don Pipo")
#         mozo1 = Mozo("Juan")
#         mozo2 = Mozo("Pedro")
        
#         # Procesar pedidos
#         maestro.tomar_pedido(orden1)
#         maestro.cocinar()
#         pizzas_entregadas = maestro.entregar(orden1)
        
#         mozo1.tomar_pizzas(pizzas_entregadas)
#         mozo1.servir_pizzas()
        
#         # Mostrar estados y costos
#         print(f"Estado de la orden: {orden1.obtener_estado_orden()}")
#         print(f"Costo total de la orden: {orden1.calcular_total()}")

# if __name__ == '__main__':
#     tester_pizzeria = TesterPizzeria()
#     tester_pizzeria.main()


# class TesterPizzeria:
#     def main(self):
#         maestro_pizzero = MaestroPizzero("Alfredo")
#         mozo1 = Mozo('Juan')
#         mozo2 = Mozo('Carlos')

#         print("Bienvenidos a pizzería de Don Pipo, este es nuestro menú:""\n" +"\n".join(Pizza.VARIEDADES))

#         pizzas_selected = self.UserElection()

#         maestro_pizzero.tomarPedido(pizzas_selected)
#         maestro_pizzero.cocinar()

#         pizzas_cooked = maestro_pizzero.entregar(pizzas_selected)
#         pizzas_restantes =  []

#         if mozo1.obtenerEstadoLibre():
#             pizzas_restantes = mozo1.tomarPizzas(pizzas_cooked)  # Mozo 1 toma hasta 2 pizzas
#             mozo1.servirPizzas()

#         if pizzas_restantes and mozo2.obtenerEstadoLibre():
#             mozo2.tomarPizzas(pizzas_restantes)  # Mozo 2 toma las restantes
#             mozo2.servirPizzas()


#     def UserElection(self):
#         election = input("Por favor ingrese el número de la/s pizza/s elegida/s: (ej: 1,3) ")
#         self.limpiar_consola()
#         selected = []
    
#         for i in election.split(','):
#             if i.isdigit():
#                 numero = int(i)
#                 if 1 <= numero <= len(Pizza.VARIEDADES):
#                     selected.append(Pizza.VARIEDADES[numero])
#                 else:
#                     print(f"'{i}' no es un número válido.")
#         return selected
    
#     def limpiar_consola(self):
#         if platform.system() == "Windows":
#             os.system("cls")
#         else:
#             os.system("clear") 

# if __name__ == '__main__':
#     testerPizzeria = TesterPizzeria()
#     testerPizzeria.main() 




# from MaestroPizzero import MaestroPizzero
# from Mozo import Mozo
# from Pizza import Pizza
# from PizzaVariedad import PizzaVariedad
# from Orden import Orden
# copilot

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
        maestro.tomar_pedido(orden1)
        maestro.cocinar()
        pizzas_entregadas = maestro.entregar(orden1)
        
        mozo1.tomar_pizzas(pizzas_entregadas)
        mozo1.servir_pizzas()
        
        # Mostrar estados y costos
        print(f"Estado de la orden: {orden1.obtener_estado_orden()}")
        print(f"Costo total de la orden: {orden1.calcular_total()}")

if __name__ == '__main__':
    tester_pizzeria = TesterPizzeria()
    tester_pizzeria.main()

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
