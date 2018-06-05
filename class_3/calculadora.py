#!/usr/bin/env python
#!coding=utf-8

print('''
	\t \t ***    CALCULADORA     ***
	Ingresa la letra que corresponda a la opcion deseada
		\t a. Sumar
		\t b. Restar
		\t c. Dividir
		\t d. Multiplicar
	''')
option = input()
if not((option == 'a') or (option =='b') or (option =='c') or (option =='d')):
	# print(type (option), print)
	print('Por favor introduce una opción VÁLIDA e intentalo nuevamente')
	quit()

print('Ingresa el 1er valor')
value_A = int(input())

print('\n Ingresa el 2do valor')
value_B = int(input())

if (option == 'a'):
	# print('Suma')
	print( '\n \t Resultado: '+ str(value_A + value_B))
elif (option == 'b'):
	# print('Resta')
	print( '\n \t Resultado: '+ str(value_A - value_B))
elif (option == 'c'):
	# print('División')
	print( '\n \t Resultado: '+ str(value_A / value_B))
elif (option == 'd'):
	# print('Multiplicacion')
	print( '\n \t Resultado: '+ str(value_A * value_B))
