# Pyhton
	Datos curso: 
		dev.aaron.gh@gmail.com
		### T1
			1. Feedback
			2. Proyecto Final (procesador de datos)
				2.1. Buscar librerías
			3. Enviar archivo.py con lo aprendido en clase

		Revisar:
			bit.ly/unipain (presentación Ned Bachter)
		### Práctica 
		phicer -> JS p/ juegos

	Lenguaje dinámico.
## Clase 1


Lenguaje de programación: lenguaje formal, instrucciones, sintaxis, resultado.
	Forma en la que expresamos como realizar una *serie de instrucciones* (forman un programa).

	Sintaxis:  determina las reglas que se siguen /  set de reglas, principios y procesos que gobiernan --- un lenguaje.
	
	Palabras reservadas (set detereinado de palabras que cumplen una tarea especifica) = token (abstracción de lo que representa) 
		- reservados: los que ya están definidos
		- declarados: los que uno declara para cumplir una función ( variables, funciones, ... , etc );

		identificadores (myVar), key words (if), separadores(token punto), operadores, literales (tipos de datos, numericas, logicas, de referencia (var2 = var), comentarios (notas para nuestro yo del futuro))

Tipos de lenguajes de programación

	Compilado (bajo nivel): usa el resultado de la compilación
		Hablan directamente con el HW, en binario
		Más rápido (los compiladores los optimizan)
		Más complejo

	Interpretado (alto nivel):
		Traducido o ejecutado (no hay algo que lo convierta a binario)
		Más lento
		Más entendible

	Nivel se refiere a que tan cerca está al sistema binario.


Maquina virtual: sistema dentro de otro sistema


### VALOR AGREGADO: tener la habilidad de resolver un problema. 
Incrementa nuestra productividad

	1. Contexto:
	2. Objetivo
	3. Fases: describir QUÉ es lo que se necesita
	4. Diseño: describir CÓMO es que se va a realizar 
	5. Implementación: 


	*Espacios*: para delimitar bloques de código / scope de código
	*#*: comentarios de 1 línea
	*""*: comentarios multilínea
	*Convenciones para nombrar variables*: (misma JS)
		Identifica el tipo de dato
			nameVariable = 'valor' / "valor"
			nameVariable = 0123
			nameVariable = list()
			nameVariable = []
if for def else 


*** Comandos
	
		dir / ls -> lista los directorios
		cd \ 
		del / rm -> borrar ARCHIVOS
		rmdir/ rm -r nombreCarpeta -> Borrar CARPETAS
			-r indica recursividad

		>>> -> todo después de esto son comandos de PYTHON

		Para ejecutar un programa:
			1. Ubicarnos en la ubicación del archivo
			2. Ejecutar comando
				./nombre_archivo.py (ejecuta lo que tiene el programa)

				python nombre_archivo.py




### SINTAXIS 

	miNombre = 'Inti'
>>>miNombre // 'Inti'
	-> muestra el retorno del valor de la ejecución
>>>print(miNombre) //Inti
	-> indica una impresión tal cual

	mult = 3*3
>>>mult // 9
>>>print(mult) // 9 

>>>token = ( ) 
-> se utiliza para indicar que escribiremos en varias líneas (al dar enter aparecen ...)

	word1 = 'Hola '
	word2 = 'Inti'

>>>oracion = ( 
...		word1 + word2 //no olvidar el tab
) //cierra el "proceso" para escribir multilínea
>>>oracion // 'Hola Inti'



## Clase 2: tipos de datos.

	"En PYTHON todo es un objeto"
	"Siempre identificar con que tipo de dato se está trabajando"

		-type
		-int
		-byte
		-float
		-bool

	Shebangs #! (todos los archivos .py tienen que comenzar con las siguientes líneas(indica que se está trabajando con un sccript))
		#!/usr/bin/env/ python -> esta linea puede causar problemas en algunos equipos, si es así, se puede omitir. 
		#coding=utf-8

	Comentarios (se puede utilizar #, """, ''')
		#Esto es un comentario de 1 línea

		''' Esto es un comentario multi
		línea
		'''

	>Objetos
		- etiqueta (nombre que se le asigna)
		-

		##En el Script NO escribir más de 79 caracteres

	Tipos strings (cadena de caracteres) en Python
		Unicode (convención -> utf-8)
		- str
		- byte

	Para pasar de:
		 string -> byte ENCODE (m de strings)

		 byte -> string DECODE (md byte)

		 index= te indica la posición de los elememntos 

	Tipos de datos númericos:
		- float 0.xxxxxx (todo dato númerico con punto)
		- int 0

		La operación DIVISIÓN SIEMPRE regresa por default un tipo de dato FLOTANTE

	Tokens booleanos:
		- and
		- not 
		- or
		- is pequivalente al === de JS (compara valor, tipo de dato y prototype)

		if variable is None

		true == 1 -> true