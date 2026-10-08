vector=[]
nombre=input("ingrese nombre")
diccionario1 = {"nombre": nombre, "edad": 25,"dni": 12345678}
diccionario2 = {"nombre": "Ian", "edad": 16}
#sintaxis de diccionario: {clave1: valor1, clave2: valor2, ...}

# Agregar diccionarios a la lista
vector.append(diccionario1)
vector.append(diccionario2)
vector.append({"nombre":nombre,"edad":20,"dni":120349})


for i in range(len(vector)):
    if vector[i]["edad"]>18:
        print
    n=vector[i]["nombre"]
    dni=vector[i]["dni"]
    pri_nom=n[:2]
    d=str(dni)[::-1]
    token=pri_nom+d    