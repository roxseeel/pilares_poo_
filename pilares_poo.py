#ENCAPSULAMIENTO
class Persona:
#Esta clase define una entidad Persona con atributos para almacenar su nombre y edad. También incluye métodos para obtener y modificar estos atributos.
    def _init_(self, nombre, edad):
#Constructor de la clase Persona.Inicializa los atributos nombre y edad de la persona.
        #Parámetros:
            #nombre (str): El nombre de la persona.
            #edad (int): La edad de la persona.
        self._nombre = nombre
        self._edad = edad
    def obtener_nombre(self):
        #Devuelve el nombre de la persona.
        return self._nombre
    def obtener_edad(self):
        #Devuelve la edad de la persona.
        return self._edad
    def set_edad(self, nueva_edad):
        #Establece la nueva edad de la persona.
        #Parámetros:
            #nueva_edad (int): La nueva edad a asignar.
        #Valida si la edad proporcionada es válida (mayor o igual a 0).
        #Si la edad es válida, la asigna al atributo _edad.
        #Si la edad no es válida, imprime un mensaje indicando que la edad no es válida.
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("Edad no válida")
#HERENCIA
class Estudiante(Persona):
    #Esta clase hereda de la clase Persona y define una entidad Estudiante con atributos para almacenar su nombre, edad y curso.
    #También incluye métodos para obtener el curso del estudiante.
    def _init_(self, nombre, edad, curso):
        #Constructor de la clase Estudiante.
        #Inicializa los atributos nombre y edad heredados de la clase Persona y el atributo curso específico de la clase Estudiante.
        #Parámetros:
            #nombre (str): El nombre del estudiante.
            #edad (int): La edad del estudiante.
            #curso (str): El curso al que pertenece el estudiante.
        super()._init_(nombre, edad)  # Se llama al constructor de la clase padre (Persona)
        self.curso = curso
    def obtener_curso(self):
        #Devuelve el curso del estudiante.
        return self.curso
#POLIMORFISMO
class Animal:
    #Esta clase define una entidad animal genérica con la capacidad de comer.
    #Métodos:
        #comer(comida): Imprime un mensaje indicando que el animal está comiendo la comida especificada.
    def comer(self, comida):
        #Imprime un mensaje indicando que el animal está comiendo la comida especificada.
        #Parámetros:
            #comida (str): La comida que el animal está comiendo.
        print(f"El animal está comiendo {comida}")
class Perro(Animal):
    #Esta clase hereda de la clase Animal y define una entidad perro con un comportamiento específico para comer croquetas.
    #Métodos:
        #comer(comida): Si la comida es "croquetas", imprime un mensaje indicando que el perro está comiendo croquetas con gusto.
            #Si la comida no es "croquetas", llama al método comer de la clase padre (Animal).
    def comer(self, comida):
    #Si la comida es "croquetas", imprime un mensaje indicando que el perro está comiendo croquetas con gusto.
        #Si la comida no es "croquetas", llama al método comer de la clase padre (Animal).
        #Parámetros:
            #comida (str): La comida que el perro está comiendo.
        if comida == "croquetas":
            print("El perro está comiendo croquetas con gusto")
        else:
            super().comer(comida)
class Gato(Animal):
    #Esta clase hereda de la clase Animal y define una entidad gato con un comportamiento específico para comer pescado.
    #Métodos:
        #comer(comida): Si la comida es "pescado", imprime un mensaje indicando que el gato está disfrutando de un delicioso pescado.
                #Si la comida no es "pescado", llama al método comer de la clase padre (Animal).
    def comer(self, comida):
        #Si la comida es "pescado", imprime un mensaje indicando que el gato está disfrutando de un delicioso pescado.
                #Si la comida no es "pescado", llama al método comer de la clase padre (Animal).
        #Parámetros:
            #comida (str): La comida que el gato está comiendo.
        if comida == "pescado":
            print("El gato está disfrutando de un delicioso pescado")
        else:
            super().comer(comida)
#ABSTRACCION
from abc import ABCMeta, abstractmethod
# Clase base abstracta que define la interfaz para objetos de tipo Foo
class AbstractFoo(metaclass=ABCMeta):
    #Esta clase base abstracta define la interfaz para objetos que representan entidades de tipo Foo.
    #Asegura que todas las subclases implementen el método obligatorio bar().
    @abstractmethod
    def bar(self):
        #Este es un método abstracto que debe ser implementado por cualquier subclase concreta de AbstractFoo.
        #Su comportamiento específico dependerá de la subclase.
        pass
    @classmethod
    def _subclasshook_(cls, C):
        #Gancho personalizado de subclases para imponer el requisito de implementar bar() en las subclases.
        #Este método se llama cada vez que una clase intenta heredar de AbstractFoo.
        #Devuelve:
            #True si la subclase implementa bar(), False en caso contrario.
        return (hasattr(C, 'bar') and callable(getattr(C, 'bar')) and
                issubclass(getattr(C, 'bar'), AbstractFoo.bar))
