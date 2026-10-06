A=[]
B=[]
resp=int(input("Desea cargar un empleado 1=seguir/2=detener: "))
while resp==1:
    nombre=input("ingrese nombre: ")
    apellido=input("ingrese apellido: ")
    dni=int(input("ingrese dni: "))
    empleado={"nom":nombre,"ape":apellido,"DNI":dni}#diccionario de empreado
    A.append(empleado)
    resp=int(input("Desea cargar un empleado 1=seguir/2=detener: "))

#recorrer A, bandera?, 
i=0
while i<len(A):
    j=i+1
    while j<len(A):
        if A[i]["DNI"]==A[j]["DNI"]:
            A.pop(j)
            print("Se elimino DNI repetido")
        else:
            j+=1
    i+=1

for i in range(len(A)):
    n=A[i]["nom"]
    a=A[i]["ape"]
    d=A[i]["DNI"]
    long=str(len(a))
    longn=str(len(n))
    # sumar digitos num=long+longn
    #x=str(num)
    p_a=a[:3]
    uldni=str(d)[-3:]
    token=long+longn+p_a+uldni
    #token=x+p_a+uldi
    dictoken={"ape":a,"nom":n,"dn":d,"tok":token}
    B.append(dictoken)

for i in range(len(B)-1):
    for j in range(i+1,len(B)):
        if B[i]["ape"]>B[j]["ape"]:
            aux=B[i]
            B[i]=B[j]
            B[j]=aux

for i in range(len(B)):
    print("nombre: ",B[i]["nom"])
    print("apellido: ",B[i]["ape"])
    print("DNI: ",B[i]["dn"])
    print("Token: ",B[i]["tok"])
