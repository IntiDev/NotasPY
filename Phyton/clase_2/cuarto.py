#!/usr/bin/env/ python 
#coding=utf-8

no_standar = '   This NAME es. Horrible'
#'This_Name_is_Pretty'

standar = no_standar.lower().replace(".","").strip().replace(" ","_")
# print("\""+standar+"\"")

# Ejemplo de encadenamiento de métodos
standar2 = (
	no_standar.strip(). replace('Horrible', 'Pretty')
	.title(). replace('Es.', 'es').replace(' ','_')
)

print(standar2)




