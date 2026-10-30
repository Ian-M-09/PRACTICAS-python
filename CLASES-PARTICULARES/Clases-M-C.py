"""Modelo 4: Sistema de Inventario Deportivo
Enfoque: Ordenamiento inicial utilizando cadenas de texto (alfabético).

Una tienda de deportes organiza su inventario de depósito central:

Cargar un Vector A mediante consulta interactiva (preguntando si desea continuar) con los siguientes datos: Código_Articulo (numérico), Deporte (texto) y Stock (entero).
A medida que se ingresa cada producto, se debe insertar de manera ordenada alfabéticamente por el nombre del Deporte (de la A a la Z) dentro del vector.
Se debe controlar y evitar que se carguen artículos con un Código duplicado.
Generar un Vector B a partir del Vector A. Por cada artículo, el Vector B almacenará el formato "Deporte - ID_Catálogo". El ID_Catálogo se genera automáticamente y se compone de:
Los últimos dos dígitos del Código_Articulo.
La primera y última letra del Deporte (ambas en mayúscula).
El número de Stock multiplicado por 2.
Determinar cuál es el Deporte con el menor stock total acumulado (sumando todos los artículos pertenecientes a un mismo deporte en el Vector A).
"""
A=[]
opc=input("desea seguir cargando? si/no: ")[0].upper()

while opc == "S":
    cda=input("ingrese codigo de articulo ")
    dep=input("ingrese deporte ")
    stock=input("inrese stock del articulo")
    bandera=False
    for i in range(0,len(A),3):
        if A[i]==cda:
            bandera=True
    if bandera==True:
        print("El codigo ya existe")
    else:
        pos=len(A)
        i=1# empieza en 1 porque ahi estan los deportes
        b=False
        while i<len(A) and b==False:
            if dep<A[i]:
                pos=i-1
                b=True
            i+=3
        A.insert(pos,cda)
        A.insert(pos+1,dep)
        A.insert(pos+2,stock)
    opc=input("desea seguir cargando? si/no: ")[0].upper()
    
"""
opc=input("desea seguir cargando? si/no: ")[0].upper()

while opc == "S":
    cda=input("ingrese codigo de articulo ")
    dep=input("ingrese deporte ")
    stock=input("inrese stock del articulo")
    bandera=False
    for i in range(len(A)):
        if A[i]["codigo"]==cda:
        if A[i][0]:
            bandera=True
    if bandera==True:
        print("El codigo ya existe")
    else:
        pos=len(A)
        i=0# empieza en 1 porque ahi estan los deportes
        b=False
        while i<len(A) and b==False:
            if dep<A[i]["nombre"]:
            if dep<A[i][1]
                pos=i
                b=True
            i+=1
    estuctura=[cda,dep,stock]
    A.insert(pos.estructura)
    diccionario={"codigo":cda,"deporte":dep,"Stock":stock}
    A.insert(pos.diccionario)
"""