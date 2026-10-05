"""Ejercicio: La empresa Tech Innovators S.A. quiere asignar a sus empleados códigos únicos de acceso a
la plataforma interna de proyectos. Para ello, se debe realizar un programa para las siguientes tareas:
a) Cargar un Vector A con la lista de empleados: nombre, apellido y número de documento (DNI). La
carga se realiza con una consulta interactiva al usuario, donde se le pregunta si desea seguir cargando
empleados. Además, los datos que se ingresan al vector se deben ir ordenando por DNI, en cada
iteración. También deberá controlar que no se carguen empleados con el mismo DNI.
b) Generar un vector B que, por cada empleado, almacene apellido-nombre y el código de acceso. Este
código se forma con: los últimos tres dígitos del DNI + la primera letra del apellido + la primera
letra del nombre + longitud del apellido (si el apellido tiene espacios también se cuenta).
c) Ordenar el vector B por apellido-nombre.
d) Mostrar el vector B (nombre + apellido + codigo)
Observaciones:
• Usar sólo programación en Python.
• Puede usar cualquier función adicional de Python, siempre cuando describa de manera general que realiza
y que librería incorpora.
• En el inciso a) no debe cargar los datos y al final ordenar. Se va ordenando a medida que se ingresa."""

v=[]
rta=input("ingrese opcion: si/no: ")[0]
while rta=="s":
    nom=input("ingrese el nombre: ")
    ape=input("ingrese apellido: ")    
    DNI=int(input("ingrese DNI: "))
    b=False             
    for i in range (len(v)):
            if v[i][2]==DNI:#comparo los dni cargados con el nuevo que se quiere ingresar
                print("El DNI ya se encuentra en la lista, ingrese otro")
                DNI=int(input("ingrese DNI: "))#si es que el dni ya estaba en la lista pido otro
                v.append([nom,ape,DNI])#cargo el nuevo socio con el nuevo dni
                b=True#bandera en verdadero para que no se vuelva a cargar el mismo socio
            if b==False:# si la bandera permanece en falso es porque el dni no estaba en la lista y se puede cargar el socio
                v.append([nom,ape,DNI])
#===============
""""
for i in range (len(v)): 
        if v[i][2]==DNI:#comparo los dni cargados con el nuevo que se quiere ingresar
            print("El DNI ya se encuentra en la lista, ingrese otro")
            DNI=int(input("ingrese DNI: "))
            v.append([nom,ape,DNI])
    else:
        v.append([nom,ape,DNI])
    aux=v[i]
    j=i-1
    while(aux<v[j] and j>=0):
        v[j+1]=v[j]
        j=j-1
    v[j+1]=aux
print("ordenado por insercion:",v)

"""
    