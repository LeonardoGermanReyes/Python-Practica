
print("Programa de Python de un Menu con Multiples Opciones")
import math
#Para facilitar el proceso se utilizara la funcion de "def" y la funcion "menu" hara de una especie de switch para poder elegir la opcion
def menu():
    print("\nMenu de Opciones:")
    print("1. Suma de 'n' Numeros")
    print("2. Producto entre 'n' Numeros")
    print("3. Division entre 2 Numeros")
    print("4. Calcular el Factorial de un Numero")
    print("5. Tablas de Multiplicar")
    print("6. Calculo del Cuadrado y Cubo de un Numero")
    print("7. Determinar el Promedio de una Serie de Numeros")
    print("8. Valores Maximo, Minimo y Total de Numeros Ingresados")
    print("9. Salir del Menu")

def suma_numeros():
    #Se usara la funcion "list" para una vez dentro del menu agregar los numeros en forma sucesiva y "map" para que la serie de numeros pueda ser colocada con espacios
    #La funcion ".split" hara que los numeros esten divididos
    #La "f" se usara para hacer el codigo mucho mas limpio para que dentro de las cadenas de texto se hagan las evaluaciones directamente desde ahi y no consumir mucho espacio
    numeros = list(map(float, input("Introduce los Numeros Separados por Espacio: ").split()))
    print(f"La Suma es: {sum(numeros)}")

def producto_numeros():
    numeros = list(map(float, input("Introduce los Numeros Separados por Espacio: ").split()))
    producto = 1
    for num in numeros:
        producto *= num
    print(f"El Producto es: {producto}")

def division():
    #Para la division, factorial y los siguientes se usara la sentencia "try" y "except" las cuales seran de ayuda para poder manejar errores como excepciones ya que cuando
    #la setencia de "try" falle soltara el "except" y nos dira el error en caso de alguna falla cuando ingreses los datos
    try:
        num1 = float(input("Introduce el Dividendo: "))
        num2 = float(input("Introduce el Divisor: "))
        if num2 == 0:
            print("Error la Division entre Cero")
        else:
            print(f"El Resultado de la Division es: {num1 / num2}")
    except ValueError:
        print("Error Por Favor Introduce Valores Numericos que sean Validos")
