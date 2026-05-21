""" 
1) Dado un número natural x, mostrar su último dígito.
"""
x=int (input("ingrese un numero: "))
dig=x%10
print("el ultimo digito es: ",dig)

"""2) Dado un número natural x, mostrar todos sus dígitos del menos significativo al más
significativo. """

z=int (input("ingrese un numero: "))

while z>0:
    dig=z%10
    print(dig)
    z=z//10 # la // es la division entera, remplaza la / de C
    
"""
3) Dado un número natural x, contar la cantidad de dígitos que posee
"""
c=int (input("ingrese un numero: "))
cont=0
while c>0:
    dig=c%10
    cont+=1
    c=c//10
print(cont)

"""4) Dado un número natural x, contar la cantidad de dígitos pares e impares que posee"""
