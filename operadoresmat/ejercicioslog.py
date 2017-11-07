#!/usr/bin/python
# -*- coding: utf-8 -*-

x = int(input ("Ingrese un número X \n"))
y = int(input ("Ingrese un número y \n"))

if x % y == 0:
    print("Es exacta")
else:
   print("No es exacta")


x = int(input ("Ingrese un numero X \n"))
y = int(input ("Ingrese un numero y \n"))

if x > y:
    print("Tu numero" , x , "es el mayor" , y , "es el menor")
else:
    print("Tu numero" , y , "es el mayor" , x , "es el menor")


x = int(input ("Escribe el año actual \n"))
y = int(input ("Escribe cualquier año \n"))

diferencia= x - y

if diferencia == 1:
    print("Desde el año" , x , "han pasado" , diferencia , "años")
