
# Variables y tipos básicos
edad = 16              # int
precio = 19.99         # float
nombre = "Carlos"      # str
activo = True          # bool (con mayúscula)

# Condicionales (if / elif / else)
if edad >= 18:
    print(f"{nombre} es mayor de edad")  # f-string para formatear texto
elif edad > 13:
    print("Es adolescente")
else:
    print("Es menor")

# Bucles básicos
for i in range(5):     # Genera números del 0 al 4
    print(i)

contador = 3
while contador > 0:
    print(contador)
    contador -= 1

# Funciones
def saludar(persona, saludo="Hola"):
    return f"{saludo}, {persona}!"

print(saludar("ian"))

#VECTORES  
# Creación
numeros = [10, 20, 30, 40, 50]
vacio = []

# Indexación (empieza en 0, admite índices negativos desde el final)
primer = numeros[0]    # 10
ultimo = numeros[-1]   # 50

# Slicing (rebanado): [inicio : fin_excluido : paso]
sub_vector = numeros[1:4]   # [20, 30, 40]
invertido = numeros[::-1]   # [50, 40, 30, 20, 10]

vec = [1, 2, 3]

# Agregar elementos
vec.append(4)          # [1, 2, 3, 4] -> agrega al final (O(1))
vec.insert(1, 99)      # [1, 99, 2, 3, 4] -> inserta en el índice 1
vec.extend([5, 6])     # [1, 99, 2, 3, 4, 5, 6] -> concatena otra colección

# Eliminar elementos
vec.pop()              # Quita y retorna el último elemento (6)
vec.pop(1)             # Quita el elemento en el índice 1 (el 99)
vec.remove(3)          # Busca y elimina la primera aparición del valor 3
# del vec[0]           # También elimina por índice

# Búsqueda y orden
posicion = vec.index(2) # Retorna el índice donde está el valor 2
existe = 2 in vec       # Retorna True si el elemento está en la lista

vec.sort()              # Ordena la lista en el lugar (in-place)
vec.sort(reverse=True)  # Orden descendente
vec.reverse()           # Invierte el orden in-place

datos = [4, 1, 9, 2, 8]

longitud = len(datos)   # 5
maximo = max(datos)     # 9
minimo = min(datos)     # 1
suma = sum(datos)       # 24
ordenada = sorted(datos)# Retorna una NUEVA lista ordenada sin tocar 'datos'

frutas = ["manzana", "banana", "cereza"]

# Recorrido directo por valor
for fruta in frutas:
    print(fruta)
# fruta es una variable temporal que toma el valor de cada elemento en cada iteracion

# Recorrido con índice y valor simultáneamente (muy usado)
for idx, fruta in enumerate(frutas):
    print(f"Posición {idx}: {fruta}")

# Comprensión de listas (List Comprehension) - Crear vectores en una línea
cuadrados = [x**2 for x in range(1, 6)]           # [1, 4, 9, 16, 25]
pares = [x for x in range(10) if x % 2 == 0]      # [0, 2, 4, 6, 8]

# ==========================================
# 1. ORDENAMIENTO POR SELECCIÓN
# ==========================================
arr_seleccion = [64, 25, 12, 22, 11]
n = len(arr_seleccion)

for i in range(n-1):
    j=i+1
    for j in range(n):
        if arr_seleccion[i] > arr_seleccion[j]:
            aux=arr_seleccion[i]
            arr_seleccion[i]=arr_seleccion[j]
            arr_seleccion[j]=aux
print("Ordenado por seleccion:", arr_seleccion)

# ==========================================
# 2. ORDENAMIENTO POR INSERCIÓN
# ==========================================

n=int(input("ingrese el tamaño del vector:"))
v=[]
v.append(int(input("ingrese el primer numero:")))
for i in range (1,n): #i tiene que empezar en 1 porque ya se ingreso el primer numero
    v.append(int(input(f"ingrese el numero {i+1}:")))
    aux=v[i]
    j=i-1
    while(aux<v[j] and j>=0):
        v[j+1]=v[j]
        j=j-1
    v[j+1]=aux
print("ordenado por insercion:",v)

# ==========================================
# 3. ORDENAMIENTO POR BURBUJA
# ==========================================
arr_burbuja = [64, 25, 12, 22, 11]
n = len(arr_burbuja)

for i in range(n):
    for j in range(n-1,i,-1):# lo que esta haciendo range es recorrer el arreglo de atras hacia adelante range(inicio, fin, paso) y el paso es negativo para que vaya de atras hacia adelante
        if arr_burbuja[j] < arr_burbuja[j-1]:
            aux=arr_burbuja[j]
            arr_burbuja[j]=arr_burbuja[j-1]
            arr_burbuja[j-1]=aux

print("Ordenado por burbuja:", arr_burbuja)
# ==========================================
# 4. BÚSQUEDA LINEAL
# ==========================================
arr_lineal = [64, 25, 12, 22, 11]
objetivo = 22
i=0
while i<len(arr_lineal) and arr_lineal[i]!=objetivo:
    i+=1
if i<len(arr_lineal):
    print(f"Búsqueda lineal: elemento {objetivo} encontrado en el índice {i}")
else:
    print(f"Búsqueda lineal: elemento {objetivo} no encontrado")

# ==========================================
# 5. BÚSQUEDA BINARIA (requiere arreglo previamente ordenado)
# ==========================================
arr_binaria = [11, 12, 22, 25, 64]  # Arreglo ya ordenado
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
#ingresar un nuevo elemento con .append
v=[]#no tiene un tamaño definido ni elementos
while prod==1:
    consumos=str(input("ingrese el tipo de consumo (producto): "))
    v.append(consumos)
    print()
    prod=int(input("Desea cargar productos?: 1=seguir, 2=detener "))

vec_nvo=[]

for i in range(len(v)):#toma cada elemento de v y lo guarda en consumo para compararlo 
    b=False
    #en ciclos anidados los indices deben ser distintos
    for j in range(len(vec_nvo)):#recorro vec_nvo para ver si el consumo ya esta en vec_nvo
        if vec_nvo[j][0]==v[i]:#el nec_nvo es una estructura de datos que tiene 2 elementos, el primero es el tipo de consumo y el segundo es la cantidad de veces que se repite
            vec_nvo[j][1]+=1# basicamente es una estructura donde con [1] accedo al contador de cada tipo de consumo
            b=True
    if b==False:#se agrega un nuevo elemento si es que no lo encuentra en vec_nvo
        vec_nvo.append([v[i],1])#agrega un nuevo elemento donde v[i] es el tipo de consumo y 1 es la segunda posicion que es el contador de veces que se repite ese tipo de consumo
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
#indice= variable (no interesa el nombre)
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
    
    print(f"Búsqueda binaria: elemento {objetivo} encontrado en el índice {med}")
else:
    print(f"Búsqueda binaria: elemento {objetivo} no encontrado")
