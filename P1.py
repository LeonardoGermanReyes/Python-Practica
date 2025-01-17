
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

def factorial():
    try:
        num = int(input("Introduce un Numero Entero: "))
        if num < 0:
            print("El Factorial no esta Definido para Numeros Negativos")
        else:
            print(f"El Factorial de {num} es: {math.factorial(num)}")
    except ValueError:
        print("Error Por Favor Introduce un Numero Entero Valido")

def tablas_multiplicar():
    try:
        num = int(input("Introduce un Numero para la Tabla de Multiplicar (del 1 al 10): "))
        if 1 <= num <= 10:
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
        else:
            print("Error Por Favor Introduce un Numero entre 1 y 10")
    except ValueError:
        print("Error has Introducido un Numero no Valido")

def cuadrado_cubo():
    try:
        num = float(input("Introduce un Numero: "))
        print(f"El Cuadrado de {num} es: {num ** 2}")
        print(f"El Cubo de {num} es: {num ** 3}")
    except ValueError:
        print("Error Por Favor Introduce un Numero Valido")

def promedio():
    #Se usara "numeros" para crear una lista de los numeros que se agreguen
    numeros = []
    while True:
        try:
            num = float(input("Introduce un Numero: "))
            if num == -1:
                break
            #La sentencia de ".append" hara que los numeros mientras no sea -1 los vaya guardando en la lista 
            numeros.append(num)
        except ValueError:
            print("Error Por Favor Introduce un Numero Valido.")
    if numeros:
        #Se usara la funcion "len" para saber la cantidad de numeros que se ingresaron ya que el promedio
        #se hace con la suma de los numeros entre el total de estos
        print(f"El Promedio es: {sum(numeros) / len(numeros)}")
    else:
        print("No se Ingresaron Numeros para Calcular el Promedio")

def maximo_minimo():
    try:
        numeros = list(map(int, input("Introduce Numeros Enteros Separados por un Espacio: ").split()))
        if numeros:
            print(f"El Valor Maximo es: {max(numeros)}")
            print(f"El Valor Minimo es: {min(numeros)}")
            print(f"El Total de Numeros Ingresados es: {len(numeros)}")
        else:
            print("No se han Ingresado Numeros")
    except ValueError:
        print("Error Por Favor Introduce solo Numeros Enteros Validos")

def main():
    while True:
        menu()
        opcion = input("\nSelecciona una Opcion: ")
        if opcion == '1':
            suma_numeros()
        elif opcion == '2':
            producto_numeros()
        elif opcion == '3':
            division()
        elif opcion == '4':
            factorial()
        elif opcion == '5':
            tablas_multiplicar()
        elif opcion == '6':
            cuadrado_cubo()
        elif opcion == '7':
            promedio()
        elif opcion == '8':
            maximo_minimo()
        elif opcion == '9':
            print("Saliendo del programa")
            break
        else:
            print("Opcion no Valida Por Favor Intentalo de Nuevamente")

if __name__ == "__main__":
    main()
