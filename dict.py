
diccionario = {'nombre':'Carlos','edad':22,'cursos':['Python','Flask']}

print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'][0])

dic = dict(nombre= 'Nestor', apellido= 'Juarez',edad=22)
print(dic)


print("_____________")
for key,value in  diccionario.items():
    print(key + ":" + str(value))


lista_cursos = diccionario['cursos']
lista_cursos.append('Java')
print(lista_cursos)
print(diccionario)

print("_____________")
#Devuelve el número de elementos que tiene un diccionario
print(len(diccionario))

#Devuelve una lista con las claves del diccionario
print(diccionario.keys())

#Devuelve una lista con los valores del diccionario
print(diccionario.values())

#Devuelve el valor del elemento con su clave. Si no lo encuentra trae un valor por default
print(diccionario.get("nombre","Juanito"))

#Inserta un elemento al diccionario con su clave:valor
diccionario['key'] = 'value'
print(diccionario)

#Elimina el elemento por la clave
diccionario.pop('key')
print(diccionario)

#Devuelve la copia de un diccionario
diccionario2 = diccionario.copy()
print(diccionario2)

#Añade los elementos de un diccionario a otro
diccionario.update(dic)
print(diccionario)
