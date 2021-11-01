# CONVERSOR DE MONEDAS EN PYTHON

def conversor(tipo_pesos, valor_dolar):
    pesos = input("Ingrese la cantidad " + " de pesos " + tipo_pesos + ": ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """ 
Bienvenido al conversor de monedas 🤑💲

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Pesos Uruguayo
5 - Pesos Dominicano
6 - Quetzal guatemalteco

Elige una opción: """

opcion = input(menu)

if opcion == "1":
    conversor("colombianos", 3757.53)
elif opcion == "2":
    conversor("argentinos", 99.67)
elif opcion == "3":
    conversor("mexicanos", 20.55)
elif opcion == "4":
    conversor("uruguayos", 44)
elif opcion == "5":
    conversor("dominicanos", 56.46)
elif opcion == "6":
    conversor("guatemaltecos", 7.80)
else:
    print("Opción inválida")
