
""" 
1) Dado un número natural x, mostrar su último dígito."""

print("Ejercio 1")
x=int (input("ingrese un numero: "))
dig=x%10
print("el ultimo digito es: ",dig)

"""2) Dado un número natural x, mostrar todos sus dígitos del menos significativo al más
significativo. """

print("Ejercicio 2")
z=int (input("ingrese un numero: "))
while z>0:
    dig=z%10
    print(dig)
    z=z//10 # la // es la division entera, remplaza la / de C
    
"""
3) Dado un número natural x, contar la cantidad de dígitos que posee"""

print("Ejercio 3")
c=int (input("ingrese un numero: "))
cont=0
while c>0:
    dig=c%10
    cont+=1
    c=c//10
print(cont)

"""4) Dado un número natural x, contar la cantidad de dígitos pares e impares que posee"""

print("Ejercicio 4")
v=int (input("ingrese un numero: "))
dp=0;di=0
while v>0:
    dig=v%10
    if dig%2==0:
        dp+=1
    else:
        di+=1
    v=v//10
print("cantidad de digitos pares: ",dp," cantidad de digitos impares: ",di)

"""5) Dado un número natural x, sumar todos sus dígitos. Mostrar la suma obtenida. """

p=int(input("ingrese un numero: "))
acu=0
while p>0:
    dig=p%10
    acu=acu+dig
    p=p//10
print("La suma de sus digitos es: ",acu)

"""6) Dado un número natural x, determinar si es capicúa."""

i=int(input("ingrese un numero: "))
cap=0
aux=i
while aux>0:
    dig=aux%10
    cap=cap*10+dig
    aux=aux//10
if i==cap:
    print("El numero ",i,"es capicua")
else:
    print("El numero",i,"no es capicua")

"""7) Dado un número natural x, mostrar todos sus divisores, contar sus divisores y sumar todos
sus divisores."""

x=int(input("Ingrese un numero: "))
cont=0
acu=0
for i in range(1,x+1):
    if(x%i==0):
        print("Un divisior es",i)
        cont+=1
        acu=acu+i
print("la cantidad de divisores es: ",cont,"y la suma de todos es: ",acu)        

"""8) Dados dos números naturales A y B, mostrar sus divisores comunes"""

a=int(input("ingrese el numero A: "))
b=int(input("ingrese el numero B: "))
men=a
ban=0
if(b<men):
    men=b
    ban=1

for i in range(1,men+1):
    if(men%i==0):
        if(ban==1):
            if(a%i==0):
                print("El numero ",i,"es divisor de ambos numeros")
        else:
            if(b%i==0):
                print("El numero ",i,"es divisor de ambos numeros")

"""9) Dados dos números naturales A y B, mostrar su máximo común divisor"""

A=int(input("ingrese el numero a: "))
B=int(input("ingrese el numero b: "))
may=A
ban=0
mayor=0
if b>may:
    may=B
    ban=1
for i in range(1,may+1):
    if(may%i==0):
        if(ban==1):
            if A%i==0:
                if i>mayor:
                    mayor=i
        else:
            if B%i==0:
                if i>mayor:
                    mayor=i
print ("El maximo comun divisor es: ",mayor)

"""10) Dada una lista de N números naturales x, mostrar el mayor de ellos."""

N=int(input("Ingrese el tamaño: "))
may=0
for i in range(1,N+1):
    var=int(input("ingrese el numero x: "))
    if(var>may):
        may=var
print("El mayor de la lista es: ",may)

"""11) Dada una lista de N números naturales x, mostrar el menor de ellos y calcular su promedio.
Mostrar el resultado."""

K=int (input("Ingrese el tamaño de la lista: "))
var=int(input("Ingrese un numero: "))
men=var 
prom=var
for i in range(2,K+1):
    var=int(input("Ingrese un numero: "))
    if(var<men):
        men=var
    prom=prom+var 
prom=prom//K
print("El promedio es: ",prom,"y el menor es: ",men)

"""12) Dada una lista ordenada de N números x, indicar si hay elementos repetidos. """

tam=int(input("Ingrese el tamaño: "))
v=int(input("Ingrese un numero: "))
auv=v
b=0
for i in range(2,tam+1):
    v=int(input("Ingrese un numero: "))
    if(auv==v):
        b=1
    auv=v
if b==1:
    print("Hay elementos repetidos")
