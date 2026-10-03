"""#tipado dinamico:# Variables y tipos básicos
edad =int(input("ingrese su edad: "))              # int (numero entero)
precio = 19.99         # float (nuemro real)
nombre = str(input("ingrese su nombre: "))      # str (cadena de texto)
activo = True          # bool (con mayúscula) (verdadero o falso) (bandera )
x=input("ingrese una palabra: ") 
print(x)

#determinar menores:
b=True
v=[10,2,5,3]

for i in range(len(v)):
    if b==True:#(si)  
        men=v[i]
        b=False
    elif b==4:#si lleva una condicion (sino)
        print("No es un bool")
    else: #no hay condicion (no)
        print("B no es verdadero, men ya tiene un valor")
    if v[i]<men:
        men=v[i]   
print ("el menor es:", men)

# Condicionales (if / elif / else)
if edad >= 18:
    print(f"{nombre} es mayor de edad")  # f-string para formatear texto
elif edad > 13:
    print(f"{nombre} es adolescente")
else:
    print(f"{nombre} es menor")

# Funciones
p=str(input("ingrese su nombre: "))
def saludar(persona, saludo="Hola"):
    return f"{saludo}, {persona}!"
print(saludar(p))

sexo=input("ingrese una palabra: ")[0]  # Toma la primera letra
print(sexo)"""
#---------------------------------------------------
#segundo parcial 09/10/2025
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
    