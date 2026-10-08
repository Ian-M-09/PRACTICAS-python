"""jercicio: Se debe realizar un programa a los fines de gestionar las credenciales de acceso (password) 
a la plataforma virtual del Club Deportivo Grand Bourg. 
En base a ello, se debe: 
a) Cargar un Vector A con la lista de Socios: Apellido, Nº documento y disciplina. El criterio de 
corte responde a un cuadro de diálogo donde se consulta al usuario si desea seguir cargando 
datos. La carga finaliza cuando se responde negativamente. No se debe permitir registrar socios con 
el mismo DNI. 
b) Generar un Vector B con Apellido, Nº documento, y la nueva credencial de acceso que se 
compone de la siguiente manera: longitud del apellido + 2 primeros caracteres del Apellido + 
3 últimos dígitos del Nº documento. 
c) Ordenar el Vector B por Apellido y mostrar. (No debe perder los datos asociados a la misma 
persona).  
d) Generar un Vector C que me muestre la cantidad de Socios agrupados por disciplina y 
ordenados por cantidad de Socios en forma decreciente. 
"""
A=[]
B=[]
C=[]
opc=input("Desea seguir cargando? si/no: ")[0].upper()#
#upper convierte la respuesta de caracteres a mayuscula
while opc=="S":
    ape=input("Ingrese apellido: ")
    dni=int(input("Ingrese DNI: "))
    dis=input("Ingrese disiciplina: ")
    i=0
    while i<len(A):#recomiendo usar este metodo para verificar que el dni no se encuentre en la lista
        if dni==A[i]["DNI"]:
            print("El DNI esta repetido ingrese uno valido ")
            dni=int(input("Ingrese DNI: "))
            i=0 #reinicio para verificar contra toda la lista
        else:
            i+=1 #avanzo i
    socio={"apellido":ape,"DNI":dni,"disciplina":dis}#creo el diccionario luego de verificar si el dni esta bien
    A.append(socio)
    opc=input("Desea seguir cargando? si/no: ")[0].upper()  
    
"""
otra forma de verificar si el dni esta repetido
b=false
for i in range(len(A))
    if dni==A[i]["DNI"]
        print("el dni esta repetido, ingrese uno valido")
        dni=int(input("Ingrese DNI: "))
        b=True
            socio={"apellido":ape,"DNI":dni,"disciplina":dis}
            A.append(socio)
if b==False
    socio={"apellido":ape,"DNI":dni,"disciplina":dis}
    A.append(socio)
VALIDA UNA UNICA VEZ, SI EL DNI SE INGRESA MAL MAS DE UNA VEZ LA SEGUNDA VEZ QUE SE INGRESE SE LO VA A TOMAR 
COMO UN DNI VALIDO
"""

for i in range(len(A)):
    a=A[i]["apellido"]
    d=A[i]["DNI"]
    long=str(len(a))
    c_a=a[:2]
    u_d=str(d)[-3:]
    codigo=long+c_a+u_d
    sociot={"Apellido":A[i]["apellido"],"DNI":d,"credencial":codigo}
    B.append(sociot)

B.sort(key=lambda x:x["Apellido"])
"""
for i in range(len(B)-1):
    for j in range (i+1,len(B)):
        if B[i]["Apellido"]>B[j]["Apellido"]:
            aux=B[i]
            B[i]=B[j]
            B[j]=aux
"""
for i in range(len(B)):
    print("Apellido",B[i]["Apellido"])
    print("DNI: ",B[i]["DNI"])
    print("Credencial: ",B[i]["credencial"])

for i in range(len(A)):
    dep_actual=A[i]["disciplina"]
    b=False
    for j in range(len(C)):
        if C[j]["disciplina"]==dep_actual:
            C[j]["cantidad"]+=1
            b=True
    if b==False:
        dicdec={"disciplina":dep_actual,"cantidad":1}
        C.append(dicdec)

C.sort(key=lambda x:x["cantidad"], reverse=True)

for i in range(len(C)):
    print("Los deportes ordenados por cantidad son: ",C[i]["disciplina"],"la cantidad es: ",C[i]["cantidad"])