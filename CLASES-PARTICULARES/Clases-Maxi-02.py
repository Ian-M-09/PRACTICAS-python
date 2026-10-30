A=[]
opc=input("desea seguir cargando: si/no ")[0].upper()
while opc=="S":
    nombre=input("ingrese el nombre del producto: ")
    cat=input("ingrese la categoria: ")
    id_prd=int(input("ingrese ID: "))
    b=False
    for i in range(len (A)):
        if A[i]["ID"]==id_prd:
        #if A[i][0]==id_prd:
            b=True
    if b==True:
        print("el id ya existe")
    else: 
        pos=len(A)
        b1=False
        i=0
    while i < len(A) and b1==False:
        #A.sort(key=lambda c:c["ID"])
        if id_prd< A[i]["ID"]:
            pos=i
            b1=True
        i+=1
        diccionario={"ID":id_prd,"Nombre":nombre,"Categoria":cat}#te permite guardar datos de distintos tipos en una posicion del vector
        #(diccionario)estructura de datos que me permite guardar varibales/informacion, en pares de "clave":valor, al llamar a una clave me devuelve el valor asignado a esa clave
        #estruc=[id_prd,nombre,cat]
        #(estructura) estrucura de datos que me permite guardar distintas variables (distintos tipos)  
        A.insert(pos,diccionario)
    opc=input("desea seguir cargando: si/no ")[0].upper()
