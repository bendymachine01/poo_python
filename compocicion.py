# compocicon

"""Una cordenada en dos dimenciones esta compuesta por dos valores, el valor del eje delas x y el valor en el eje dela y, esto podria ser una clase. Un cuadrado esta compustos por cuatra cordenadas que son los cuatro vertices, estopodriiaserunaclase que esta compuesta por cuatroclases  del objeto cordenada."""

# clase Coordenada

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Método para mostrar la coordenada
    def mostrar_coordenada(self):
        print("(", self.x, ",", self.y, ")")

# Clase Cuadrado
class Cuadrado:
    # Constructor con 4 coordenadas
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

    # Método para mostrar los vértices
    def mostrar_vertices(self):
        print("El cuadrado está compuesto por los siguientes vértices:")
        self.v1.mostrar_coordenada()
        self.v2.mostrar_coordenada()
        self.v3.mostrar_coordenada()
        self.v4.mostrar_coordenada()

# Método principal
def main():
    # Entrada
    x1 = int(input("Digite el valor de x: "))
    y1 = int(input("Digite el valor de y: "))

    # Creación y muestra de la coordenada
    c1 = Coordenada(x1, y1)
    c1.mostrar_coordenada()

    # Creación de las coordenadas del cuadrado
    v1 = Coordenada(7, 8)
    v2 = Coordenada(10, 8)
    v3 = Coordenada(7, 5)
    v4 = Coordenada(10, 5)

    # Creación del cuadrado y muestra de sus vértices
    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrar_vertices()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
