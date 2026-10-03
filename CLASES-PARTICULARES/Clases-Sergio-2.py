V1=[]
res=int(input("desea ingresar un socio?: 1=seguir; 2=detener: "))
while res==1:
    nombre=str(input("ingrese nombre: "))
    apellido=input("ingrese apellido: ")#no hace falta el casteo input me devuelve una cadena de texto
    DNI=int(input("ingrese DNI: "))
    b=False
    for i in range (len(V1)):
        if V1[i][2]==DNI:#comparo los dni cargados con el nuevo que se quiere ingresar
            print("El DNI ya se encuentra en la lista, ingrese otro")
            DNI=int(input("ingrese DNI: "))#si es que el dni ya estaba en la lista pido otro
            sexo=input("ingrese el sexo de la persona (Masculino/Femenino):")[0]
            V1.append([nombre,apellido,DNI,sexo])#cargo el nuevo socio con el nuevo dni
            b=True#bandera en verdadero para que no se vuelva a cargar el mismo socio
    if b==False:# si la bandera permanece en falso es porque el dni no estaba en la lista y se puede cargar el socio
            sexo=input("ingrese el sexo de la persona (Masculino/Femenino):")[0]
            V1.append([nombre,apellido,DNI,sexo])
    res=int(input("desea ingresar un socio?: 1=seguir; 2=detener: "))
