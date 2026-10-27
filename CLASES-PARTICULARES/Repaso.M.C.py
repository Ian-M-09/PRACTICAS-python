B=[]
B.sort(key=lambda x:x["Apellido"])
"""
lambda palabra reservada para declarar funciones sin nombre (anonimas)
key guarda los datos que le pasa x[Apellido]
x es como el que "pasa" el dato (es la variable que se pasa como parametro a la funcino anonima definida con lambda)

"""
A=[]
for i in range(len(A)):#range(inicio,fin,paso). si quiero que salte de 2 en 2 cambio el paso a 2 y asi sucesivamente 
    a=A[i]["apellido"]#para acceder a un valor del diccionario solo necesito su clave
    d=A[i]["DNI"]
    long=str(len(a))#len me da el tamaño del apellido(cuantas letras tiene) y lo casteo a str
    c_a=a[:2]#[0:2](inicio/fin)saco las primeras 3 letras
    u_d=str(d)[-3:]#saco los ultimos 3 digitos y lo casteo a str para poder concatenar
    codigo=long+c_a+u_d
    sociot={"Apellido":A[i]["apellido"],"DNI":A[i]["DNI"],"credencial":codigo}#creacion de un diccionario
    B.append(sociot)#guardo un diccionario en el vector B

while True:
    break
    #funciona pero no es una buena practica, en lo posible no lo usen
    
opc=input("FIN para detener")
while opc!="FIN":
    print("hola")#se va a repetir siempre que el usuario ingrese cualquier cosa que no sea FIN
    opc=input("FIN para detener")
#ciclo while que se detiene si es que el usuario lo desea, se usa mas que nada para cargar vectores