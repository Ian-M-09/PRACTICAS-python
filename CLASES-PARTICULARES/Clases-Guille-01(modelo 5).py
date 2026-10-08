"""Ejercicio: Dada una lista de palabras que se debe cargar en un vector, realizar:
a) Generar otro vector B con la lista de palabras y su frecuencia de aparición.
b) Ordenar el vector B por la frecuencia de aparición de mayor a menor.
c) Insertar en el vector ordenado, y luego de la frecuencia, el porcentaje de esa frecuencia.
"""
V=[]
B=[]
opc=input("Desea seguir cargando: si/no: ")[0].upper()
while opc=="S":
    palabra=input("ingrese la palabra: ")
    V.append(palabra)
    opc=input("Desea seguir cargando: si/no: ")[0].upper()

for i in range(len(V)):
    b=False
    for j in range(len(B)):
        if B[j]["palabra"]==V[i]:
            B[j]["frecuencia"]+=1
            b=True
    if b==False:
        dicdeb={"palabra":V[i],"frecuencia":1}
        B.append(dicdeb)

B.sort(key=lambda x:x["frecuencia"],reverse=True)
"""
for i in range(len(B)-1)    
    for j in range(i=1,len(B))
        if B[i]["frecuencia"]<B[j]["frecuencia]
            aux=B[i]
            B[i]=B[j]
            B[j]=aux
"""
total=0
for i in range(len(B)):
    total=total+B[i]["frecuencia"]

for i in range(len(B)):
    p_f=(B[i]["frecuencia"]/total)*100
    B[i]["porcentaje"]=int(p_f)

for i in range(len(B)):
    print("La palabra es: ",B[i]["palabra"])
    print("La frecuencia es: ",B[i]["frecuencia"])
    print("El porcentaje es: ",B[i]["porcentaje"])
    
    