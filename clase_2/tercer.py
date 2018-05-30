pi = 3.14
pi_valor = 'El valor de pi es: '

# print(type(pi))

# Método STR para converir float a string
# print(pi_valor + str(pi))

ingles = "I'm a \"engineer\""
# print(ingles)

salto_linea = 'Esta es una línea \n esta es otra'
# print(salto_linea)

directorio = 'C:\this\name' 
directorio2 = r'C:\this\name'# con r No interpreta salto y nuevas lineas
print(3 * (directorio2 + ('\n')))

saludo = 'QUIUBO'
saludos = saludo.lower().title()

print(saludos)

#Método STRIP
prueba = 'Hola      '
print("\""+prueba.strip()+"\"")