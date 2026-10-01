
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
i=1
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