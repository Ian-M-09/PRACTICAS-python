A=[]
opc=input("desea seguir cargando: si/no ")[0].upper()
while opc=="S":
    nombre=input("ingrese el nombre del producto: ")
    cat=input("ingrese la categoria: ")
    id_prd=int(input("ingrese ID: "))
    b=False
    for i in range(len (A)):
        if A[i]["ID"]==id_prd:
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
    diccionario={"ID":id_prd,"Nombre":nombre,"Categoria":cat}
    A.insert(pos,diccionario)
    