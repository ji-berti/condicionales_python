# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temperatura_1= float(input('Ingrese una temperatura (sólo valor numérico):\n'))
temperatura_2= float(input('Ingrese otra temperatura (sólo valor numérico):\n'))
temperatura_3= float(input('Ingrese la última temperatura (sólo valor numérico):\n'))

if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
    print(f'{temperatura_1} es el mayor valor ingresado')
    if temperatura_2 > temperatura_3:
        print(f'{temperatura_3} es el mínimo valor ingresado')
    elif temperatura_2 == temperatura_3:
        print(f'tanto {temperatura_2} como {temperatura_3} son los valores mínimos ya que son iguales')
    else:
        print(f'{temperatura_2} es el menor valor ingresado')

elif temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:
    print(f'{temperatura_2} es el mayor valor ingresado')
    if temperatura_1 > temperatura_3:
        print(f'{temperatura_3} es el mínimo valor ingresado')
    elif temperatura_1 == temperatura_3:
        print(f'tanto {temperatura_1} como {temperatura_3} son los valores mínimos ya que son iguales')
    else:
        print(f'{temperatura_1} es el menor valor ingresado')


elif temperatura_3 > temperatura_1 and temperatura_3 > temperatura_2:
    print(f'{temperatura_3} es el mayor valor ingresado')
    if temperatura_1 > temperatura_2:
        print(f'{temperatura_2} es el mínimo valor ingresado')
    elif temperatura_1 == temperatura_2:
        print(f'tanto {temperatura_1} como {temperatura_2} son los valores mínimos ya que son iguales')
    else:
        print(f'{temperatura_1} es el menor valor ingresado')   

else:
    if temperatura_1 == temperatura_2 and temperatura_1 < temperatura_3:
        print(f'{temperatura_3} es el mayor valor ingresado')
        print(f'{temperatura_1} es el menor valor ingresado')
    elif temperatura_1 == temperatura_2 and temperatura_1 > temperatura_3:
        print(f'{temperatura_1} es el mayor valor ingresado')
        print(f'{temperatura_3} es el menor valor ingresado')
    elif temperatura_1 == temperatura_3 and temperatura_1 < temperatura_2:
        print(f'{temperatura_2} es el mayor valor ingresado')
        print(f'{temperatura_1} es el menor valor ingresado')
    elif temperatura_1 == temperatura_3 and temperatura_1 > temperatura_2:
        print(f'{temperatura_1} es el mayor valor ingresado')
        print(f'{temperatura_2} es el menor valor ingresado')
    elif temperatura_2 == temperatura_3 and temperatura_1 > temperatura_2:
        print(f'{temperatura_1} es el mayor valor ingresado')
        print(f'{temperatura_2} es el menor valor ingresado')
    elif temperatura_2 == temperatura_3 and temperatura_1 < temperatura_2:
        print(f'{temperatura_2} es el mayor valor ingresado')
        print(f'{temperatura_1} es el menor valor ingresado') 
    else:
        print('todos los valores ingresados son iguales')


promedio= (temperatura_1 + temperatura_2 + temperatura_3) / 3
print(f'El promedio de las temperaturas ingresadas es {promedio}')