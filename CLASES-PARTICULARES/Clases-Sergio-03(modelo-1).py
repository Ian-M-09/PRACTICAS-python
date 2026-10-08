
"""Se debe realizar un programa para gestionar la asignación de mesas en un
restaurante. Cada vez que un cliente llega, se registra su nombre, el número de personas
y el tipo de reserva (CR: con reserva, SR: sin reserva). Las reservas tienen prioridad y se
asignan primero, mientras que los clientes sin reserva se agregan al final de la lista.
En base a ello se solicita:
a) Registrar un nuevo cliente en la lista de espera. Ingresar el nombre del cliente, el
número de personas y añadirlo al principio de la lista de espera, si es un cliente
con reserva, o al final si es un cliente sin reserva.
b) Asignar una mesa a un cliente: Si una mesa está desocupada, determinar cuál es
el próximo cliente en la lista y posteriormente eliminarlo de la lista de espera.
c) Generar y mostrar un vector nuevo para mesas con x cantidad de personas
Observaciones:
• Usar sólo programación en Python.
• Puede usar cualquier función adicional de Python, siempre cuando describa de manera
general que realiza y que librería incorpora.
• Cuando ingresa un nuevo cliente con reserva en la lista de espera, debe ubicarse en la
primera posición si no existen otros. Si ya existen clientes con reserva en la lista,
debe encontrarse el último y recién a continuación debe insertarse el nuevo.
"""
lista_espera = []  # Lista de espera para clientes
vec_x=[]
opc=input("ingresar un cliente? si/no:")[0]
while opc=="s":
    nombre = input("Ingrese el nombre del cliente: ")
    num_personas = int(input("Ingrese el número de personas: "))
    tipo_reserva = input("Tiene reserva?: si/no: ")[0]
    if tipo_reserva=="s":
        b=False
        for i in range(len(lista_espera)):
            if lista_espera[i][2]=="s":
                b=True
                pos=i+1
        if b==True:
            lista_espera.insert(pos,[nombre,num_personas,tipo_reserva])
        else:
            lista_espera.insert(0,[nombre,num_personas,tipo_reserva])
    else:
        lista_espera.append([nombre,num_personas,tipo_reserva])
    opc=input("ingresar un cliente? si/no:")[0]
for i in range(len(lista_espera)):
    print()
    print("El nombre del cliente es:",lista_espera[i][0],",En total son: ",lista_espera[i][1])
print()
mesa=input("hay una mesa disponible?: si/no ")[0]
while mesa=="s" and len(lista_espera)>=0:
    lista_espera.pop(0)
    print("!Mesa libre¡, Se elimino al primero de la lista")
    mesa=input("hay una mesa disponible?: si/no ")[0]

for i in range(len(lista_espera)):
    print()
    print("El nombre del cliente es:",lista_espera[i][0],",En total son: ",lista_espera[i][1])

x=int(input("ingrese la cantidad de personas de una mesa: "))
for i in range(len(lista_espera)):
    if lista_espera[i][1]==x:
        vec_x.append(lista_espera[i])

for i in range(len(vec_x)):
    print("Los clientes con una mesa con:",x,"personas son:",vec_x[i][0])