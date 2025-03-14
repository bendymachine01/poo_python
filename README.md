# poo_python

- El paradigma de poo esta basado en una abstruccion del mndo real que nos va a premtir desarollar programas de forma mas cercana a como vemos el mundo, pensando en objtos que tenemos adelante y en aciones que podemos hacer co ellos.

## clase

- Una clase es una tipo dedato cuyas variabes se llaman objetos o instancias.
- la clase esella defiicion del concepto del mundo real y los objetos o instancias son el "propio" objeto del mundo real 

- las clases tan compuestas por dos elementos: atributos y metodos

### atributos
- informacion que almacena la clase

### metodos 
- operaciones que pueden realizaslas clases

## definicion de una clase 
```python
class NombreClase:

def _init_ (self, variable1,varable2):
self.Atributo1 = valor1
self.Atributo1 = valor1

def nombreMetodo(self):
    bloqueCodigo
```

### Componentes

```class```: palabra reservada en python para definir una clase.

```NombreClase```_: nombre de la clase que quieres crear.

```def```: plbre reserada en python que se utilza para definir tanto el constructor de la clase (metodo que se ejecut la primera vez que usas una clase) como losdiferentes metodos que tiene.

```_int_```: palabrareservaaen pythonpar deinir el metodo constructor de la clase. Es lo primero que se ejecuta cuando crear un objeto de una clase.

```(self, vasriableX)```: paraetro del constructor de la clase. El paremetro self es obligatorio y despues puedes tener tantos parametros como quiras. La forma de añadir parametros es la misma que las fuciones.

```self.AtributosX```: forma de utilizacion y acseso a los tributos de la clase.

```nombreMetodo```:

```(self)```: parametros del metedo. El paremetro self es obligatorio y despues puedes tener tantos parametros como quiras. La forma de añadir parametros es la misma que las fuciones.

```bloqueCodigo```: instucciones que ejecutara el metodo.
 - cuando defines una clase debes tener en cuenta los siguientes puntos: 
 - puedes definir tantos atributos como necesites. 
 - puedes definir tantos parametros como necesites. 
 - puedes definir tantos parametros en el constructor y en los metodos como necesites.

 ## COMPOOCICION
- Consiste en la cracion  clases clases a partir de otras ya existentes seran aribuosde la nueva clase.
- en POO lacompocicion signficaque enre las dos clases existe una racion del tipo "tiene un."
- Ejemplo:
    -   Una cordenada en dos dimenciones esta compuesta por dos valores, el valor del eje delas x y el valor en el eje dela y, esto podria ser una clase. Un cuadrado esta compustos por cuatra cordenadas que son los cuatro vertices, estopodriiaserunaclase que esta compuesta por cuatroclases  del objeto cordenada.
    