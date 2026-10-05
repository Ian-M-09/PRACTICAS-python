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
A=[]

rta=int(input("ingrese 1:seguir/2:detener: "))
while rta==1:
    nom=str(input("ingrese nombre: "))
    ap=str(input("ingrese apellido: "))
    DNI=int(input("ingrese DNI: "))
    for i in range(len(A)):
        if DNI==A[i][2]:
            print("El DNI esta repetido ingrese uno valido")
            DNI=int(input("ingrese DNI: "))
    A.append([nom,ap,DNI])
    i=len(A)-1
    aux=A[i]
    j=i-1
    while j>=0 and aux[2]<A[j][2] :
        A[j+1]=A[j]
        j=j-1
    A[j+1]=aux
    rta=int(input("ingrese 1:seguir/2:detener: "))

for i in range(len(A)):
    print("nombres:",A[i][0])
    print("apellido:",A[i][1])
    print("DNI:",A[i][2])

B=[]
for i in range(len(A)):
    nombre=A[i][0]
    apellido=A[i][1]
    DNI_t=str(A[i][2])
    codigo=DNI_t[-3:]+apellido[0]+nombre[0]+str(len(apellido))
    B.append([A[i][1],A[i][0],codigo])

for i in range(len(B)):
    aux=B[i]
    j=i-1
    while j>=0 and aux[0]<B[j][0] :
        B[j+1]=B[j]
        j=j-1
    B[j+1]=aux

for i in range(len(B)):
    print()
    print("Apellido: ",B[i][0])
    print("Nombre: ",B[i][1])
    print("Codigo: ",B[i][2])

