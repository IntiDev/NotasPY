#coding=utf-8

text_byte = b'Quiubo' #Cada 
text_str = 'Quiubo'

# print(text_byte)
# print(text_str)

# print(type(text_byte))
# print(type(text_str))

# print(text_str == text_byte.decode())

# print(type(text_byte[0]))

# INDICES 

print(text_str[0])
print(text_str[:1]) # Trae todo lo que esta del indice hacia atras/izq (no es incluyente)
print(text_str[2:]) #Trae todo lo del indice para la derecha
print(text_str[-1])
print(text_str[1:4])

print(text_str[0] + text_str[-1]) 
# print()

sku = 'ABC123'
sku = sku[:3] + '-' + sku[3:]
print(sku)