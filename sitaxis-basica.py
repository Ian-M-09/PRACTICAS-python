

edad = 16 #int            
precio = 19.99 #float         
nombre = "Carlos" #str  
activo = True #boole


if edad >= 18:#si
    print(f"{nombre} es mayor de edad")  
elif edad > 13:#sino
    print("Es adolescente")
else:#no
    print("Es menor")


for i in range(5):#sintaxis range(inicio,fin,paso)
    print(i)

contador = 3
while contador > 0:
    print(contador)
    contador -= 1


def saludar(persona, saludo="Hola"):
    return f"{saludo}, {persona}!"

print(saludar("ian"))


numeros = [10, 20, 30, 40, 50]
vacio = []


primer = numeros[0]    
ultimo = numeros[-1]   


sub_vector = numeros[1:4]  
invertido = numeros[::-1]  

vec = [1, 2, 3]


vec.append(4)#agregar al final          
vec.insert(1, 99)#agregar en una posicion sintaxis (posicion,elemento)
vec.extend([5, 6])   


vec.pop()#elimina el ultimo           
vec.pop(1)#elimino el elemento de la posicion 1             
vec.remove(3)        
# del vec[0]           


posicion = vec.index(2)#te devuelve la posicion del elemento 2 
existe = 2 in vec      

vec.sort()             
vec.sort(reverse=True)  
vec.reverse()           

datos = [4, 1, 9, 2, 8]

longitud = len(datos)#te da el tamaño
maximo = max(datos)     
minimo = min(datos)     
suma = sum(datos)       
ordenada = sorted(datos)

frutas = ["manzana", "banana", "cereza"]


for fruta in frutas:
    print(fruta)



for idx, fruta in enumerate(frutas):
    print(f"Posición {idx}: {fruta}")


cuadrados = [x**2 for x in range(1, 6)]          
pares = [x for x in range(10) if x % 2 == 0]    
#mod cambia por % y el div 0 / cambia //

arr_seleccion = [64, 25, 12, 22, 11]
n = len(arr_seleccion)

for i in range(n-1):
    for j in range(i+1,n):
        if arr_seleccion[i] > arr_seleccion[j]:
            aux=arr_seleccion[i]
            arr_seleccion[i]=arr_seleccion[j]
            arr_seleccion[j]=aux
print("Ordenado por seleccion:", arr_seleccion)



n=int(input("ingrese el tamaño del vector:"))
v=[]
v.append(int(input("ingrese el primer numero:")))
for i in range (1,n): 
    v.append(int(input(f"ingrese el numero {i+1}:")))
    aux=v[i]
    j=i-1
    while(aux<v[j] and j>=0):
        v[j+1]=v[j]
        j=j-1
    v[j+1]=aux
print("ordenado por insercion:",v)


arr_burbuja = [64, 25, 12, 22, 11]
n = len(arr_burbuja)

for i in range(n):
    for j in range(n-1,i,-1):
        if arr_burbuja[j] < arr_burbuja[j-1]:
            aux=arr_burbuja[j]
            arr_burbuja[j]=arr_burbuja[j-1]
            arr_burbuja[j-1]=aux

print("Ordenado por burbuja:", arr_burbuja)

arr_lineal = [64, 25, 12, 22, 11]
objetivo = 22
i=0
while i<len(arr_lineal) and arr_lineal[i]!=objetivo:
    i+=1
if i<len(arr_lineal):
    print(f"Búsqueda lineal: elemento {objetivo} encontrado en el índice {i}")
else:
    print(f"Búsqueda lineal: elemento {objetivo} no encontrado")


arr_binaria = [11, 12, 22, 25, 64] 
objetivo = 22
i=0
n=len(arr_binaria)
med=i+n//2
while i<=n and arr_binaria[med]!=objetivo:
    if arr_binaria[med]<objetivo:
        i=med+1
    else:
        n=med-1
    med=(i+n)//2
if i<=n:
    print(f"Búsqueda binaria: elemento {objetivo} encontrado en el índice {med}")
else:
    print(f"Búsqueda binaria: elemento {objetivo} no encontrado")

#===========================
#segundo parcial 09/10/2025
#============================
prod=int(input("Desea cargar productos?: 1=seguir, 2=detener "))
v=[]
while prod==1:
    consumos=str(input("ingrese el tipo de consumo (producto): "))
    v.append(consumos)
    print()
    prod=int(input("Desea cargar productos?: 1=seguir, 2=detener "))

vec_nvo=[]

for i in range(len(v)):
    b=False
    for j in range(len(vec_nvo)):
        if vec_nvo[j][0]==v[i]:
            vec_nvo[j][1]+=1
            b=True
    if b==False:
        vec_nvo.append([v[i],1])
"""uso de estructuras:
vec_nvo=[[producto,cantidad],[producto2,cantidad2],[producto3,cantidad3]]
accedo a producto con el [0] y a cantidad con el [1]. [j] es la posicion
si en algun momento necesito agregar otro campo a la estructura hago:
vec_nvo.append([elemento1,elemento2,elemento3])
ahora el nuevo campo accedo con [2]"""
for i in range(len(vec_nvo)):
    print()
    print("tipo de consumo:",vec_nvo[i][0],"- cantidad:",vec_nvo[i][1])

max1=0
max2=0
ind1=0
ind2=0

for i in range(len(vec_nvo)):
    if vec_nvo[i][1]>max1:
        max2=max1
        ind2=ind1
        max1=vec_nvo[i][1]
        ind1=i

print("El mas frecuente fue: ",vec_nvo[ind1][0])
print("El segundo mas frecuente fue: ",vec_nvo[ind2][0])

vec_1vez=[]

for i in range(len(vec_nvo)):
    if(vec_nvo[i][1]>1):
        vec_1vez.append(vec_nvo[i][0])

for i in range(len(vec_1vez)):
    print()
    print("Los productos que se consumieron mas de 1 vez son: ",vec_1vez[i])
