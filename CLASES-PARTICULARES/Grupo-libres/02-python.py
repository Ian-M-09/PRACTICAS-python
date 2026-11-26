"""Secuencia estrictamente creciente: Ingresar N números enteros.
Informar si fueron ingresados en orden estrictamente creciente
(cada número mayor al anterior)."""

N=int(input("Ingrese el tamaño: "))
b=False
creciente=True
for i in range(N):
    x=int(input("Ingrese el numero: "))
    if b==False:
        aux=x
        b=True
    elif x <= aux:
        creciente=False
    aux=x
if creciente==True:
    print("Es creciente")
else:
    print("No es creciente")

"""Racha más larga de positivos: Ingresar números enteros hasta que se ingrese un 0 .
calcular e informar la longitud de la racha consecutiva más larga de números positivos 
(ejemplo: en 3, 5, 2, -1, 4, 8, -2, 0 la racha más larga es 3 )."""
cont=0
racha=0
x=int(input("Ingrese un numero: "))
while x!=0:
    if x>0: 
        cont+=1
        if cont>racha:
            racha=cont
    else: 
        cont=0
    x=int(input("Ingrese un numero: "))
print("La racha mas larga es: ",racha)

"""Se ingresan notas (del 1 al 10) de los alumnos de una comision hasta que se ingrese 0 
para finalizar (validar que toda nota distinta de 0 este en rango). Al terminar informar:
1. cantidad total de alumnos evaluados y promedio general (validando si no se cargo niguno)
2. la nota mas alta y la nota mas baja
3. cantidad y porcentaje de alumnos aprobados (nota>=6) y promocionados (nota>=8)"""

cant_alm=0
cant_apro=0
cant_notas=0
cant_prom=0
b=True
nota=int(input("ingrese la nota: "))
while nota!=0:
    if nota >= 1 and nota <=10:
        cant_alm+=1
        cant_notas+=1
        if b==True:
            max_nota=nota
            min_nota=nota
            b=False
        else:
            if nota > max_nota:
                max_nota=nota
            if nota< min_nota:
                min_nota=nota
        if nota>=6:
            cant_apro+=1
        if nota>=8:
            cant_prom+=1
    else:
        print("Nota no valida")
    nota=int(input("ingrese la nota: "))
if cant_alm>0:
    promedio=cant_notas/cant_alm
    porc_apro=(cant_apro*100)/cant_alm
    porc_promocio=(cant_prom*100)/cant_alm
    print("Cantidad total de alumnos evaluados:", cant_alm)
    print("Promedio general:", promedio)
    print("Nota mas alta:", max_nota)
    print("Nota mas baja:", min_nota)
    print("Aprobados (>=6):", cant_apro)
    print("porcentaje aprobados: ", f"({porc_apro:.2f}%)")
    print("Promocionados (>=8):", cant_prom)
    print("porcentaje promocionados:", f"({porc_promocio:.2f}%)")
else:
    print("No se cargaron alumnos validos.")