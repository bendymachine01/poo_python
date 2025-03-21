# Clase base 1
class Mamifero:
    def amamantar(self):
        print("Soy un mamífero y amamanto a mis crías.")

# Clase base 2
class Volador:
    def volar(self):
        print("Puedo volar alto en el cielo.")

# Clase derivada que hereda de ambas
class Murcielago(Mamifero, Volador):
    def descripcion(self):
        print("Soy un murciélago, un mamífero que puede volar.")

# Crear un objeto de la clase Murciélago
bat = Murcielago()
bat.descripcion()
bat.amamantar()  # Método de Mamifero
bat.volar()      # Método de Volador


# Mamifero tiene un método amamantar().
# Volador tiene un método volar().
# Murcielago hereda de ambas y combina sus características.