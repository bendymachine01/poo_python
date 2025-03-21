# Encapucion

"""Una cordenada en dos dimenciones esta compuesta por dos valores, el valor del eje delas x y el valor en el eje dela y, esto podria ser una clase. Un cuadrado esta compustos por cuatra cordenadas que son los cuatro vertices, estopodriiaserunaclase que esta compuesta por cuatroclases  del objeto cordenada."""

# clase Coordenada

class Coordenada:

    # metodo constructor
    def __init__(self, x, y):
        # atributos privados
        self.__X = x
        self.__Y = y

    # metodos de lectura y escritura de cada atributo
    def getX(self):
        return self.__X
    
    def getX(self):
        return self.__Y
    
    def getX(self):
        self.__X = x
    
    def getY(self):
        self.__Y = y

    # Método para mostrar la coordenada
    def mostrar_coordenada(self):
        print("(", self.__X , ",", self.__Y, ")")

# Clase Cuadrado

class Cuadrado:

    # metodo Constructor
    def __init__(self, v1, v2, v3, v4):
        # atributos privdos
        self.__v1 = v1
        self.__v2 = v2
        self.__v3 = v3
        self.__v4 = v4

    # Métodos privados para mostrar los vértices
    def __mostrarCoordenadaV1(self):
        print("(", self.__V1.getX(),",", self.__V1.getY(),")")

    def __mostrarCoordenadaV2(self):
        print("(", self.__V2.getX(),",", self.__V2.getY(),")")
    
    def __mostrarCoordenadaV3(self):
        print("(", self.__V3.getX(),",", self.__V3.getY(),")")
    
    def __mostrarCoordenadaV4(self):
        print("(", self.__V4.getX(),",", self.__V4.getY(),")")
    
    # metodo para mosrar los vertices
    def mostrarVertices(self):
        print("El cuadrado estacompuesto por los siguietes vertices: ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()

# Método principal del modulo
def main():
    # input
    x1 = int(input("Digite el valor de x: "))
    y1 = int(input("Digite el valor de y: "))
    # processing
    c1 = Coordenada(x1, y1)
    c1.mostrar_coordenada()

    v1 = Coordenada(7, 8)
    v2 = Coordenada(10, 8)
    v3 = Coordenada(7, 5)
    v4 = Coordenada(10, 5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()

    # Que ocurre si el meodo de getX() lo hacemos privado: __getX()?
    coordenada = Coordenada(3,4)
    print("(", coordenada.getX(),",", coordenada.getY(), ")")

if __name__ == "__main__":
    main()