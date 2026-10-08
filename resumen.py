#vectores
#declaracion
V=[]
#V=[none]*n crea un vector vacio de tamaño n
#V=[none]

#insertar elementos en un vector
V.append()#inserto al final
V.insert()#inserto en una posicion en especifico
pos=2#guardo un elemento "el 30"en la posicion 4 moviendo todos los elementos un lugar a la derecha
V[pos:pos]=[30]#el elemnto se guarda en pos:1
#[10,20,40,50]

V[len(V)+1:len(V)+1]=[30]

V.append(None)#creo un lugar vacio al final del vector
for i in range(len(V)-1,pos,-1):#len(V)-1 se para donde esta el none
    V[i]=V[i-1]
#muevo todos los elementos del vector un lugar a la derecha
V[pos]=[30]#agrego el elemento que quiero en el lugar que prepare para el

V.sort(key=lambda x:x["dni"])
n=len(V)
for i in range(n-1):
    for j in range(i+1,n):
        if V[i] > V[j]:
            aux=V[i]
            V[i]=V[j]
            V[j]=aux
print("Ordenado por seleccion:", V)


V.pop()
for i in range(pos,len(V)-1):
    V[i]=V[i+1]
V=V[:-1]

#maneras de sacar elementos de una palabra dni etc.
dni=2384712498234
primero_dni=str(dni)[:3]
ultimos_dni=str(dni)[-3:]

#la sitaxis es [inicio:fin]
#si quiero los primeros el iniciio es 0 el fin 3
#si quiero los ultimos el inicio es -3 el fin es len(dni) que no hace falta poner igual que el 0
