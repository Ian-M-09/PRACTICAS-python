# int entero 
# float decimal/real
# str cadena de texto/ caracteres
# bolean verdadero o falso
# print mustra en pantalla
# input permite ingresar datos por teclado
print("Hola mundo")
x=int(input("ingrese un numero:"))
nombre=str(input("ingrese su nombre:"))
print(type(x))
print(x)

while x<5:
    print("hola", x)
    x=x+1
    
for i in range(5):
    print("hola", i)


if x >= 18:#si
    print(f"{nombre} es mayor de edad")  
elif x > 13:#sino
    print("Es adolescente")
else:#no
    print("Es menor")

aux=x
cap=0
while aux>0:
    d=aux%10
    print(d)
    cap=cap*10+d
    print(cap)
    aux=aux//10
    print(aux)
if x==cap:
    print("es capicua")
else:
    print("no es capicua")
"""
maximo = max(datos)     
minimo = min(datos)   
"""
opc=int(input("ingrese un numero:"))
b=False
while opc>0 and opc<100:
    if b==False:
        max=opc
        b=True
    if opc>max:
        max=opc
    opc=int(input("ingrese un numero:"))
print("el mayor es: ", max)