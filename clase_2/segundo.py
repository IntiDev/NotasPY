#!/usr/bin/env/ python 
#coding=utf-8

template = 'El estudiante, {} , está aprendiendo, {}'
estudiante = 'inti'
skill = 'Python'

# Método FORMAT para llenar template
mensaje = template.format(estudiante.title(), skill)

print(mensaje)