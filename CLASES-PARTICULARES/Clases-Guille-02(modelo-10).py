"""Ejercicio:  Un centro odontológico habilita la asignación de turnos todos los viernes para la semana 
siguiente. El centro cuenta con dos odontólogos: 
• Odontólogo A atiende los lunes, miércoles y viernes. 
• Odontólogo B atiende los martes y jueves. 
Ambos trabajan únicamente por la tarde, de 15:00 a 20:00 hs, lo que representa una franja de 5 horas 
(300 minutos) por día. Los pacientes llaman para solicitar turnos según el tipo de prestación requerida: 
Consulta 30 minutos, Arreglo 60 minutos y Cirugía/Estética 90 minutos. 
Los llamados se reciben de forma indefinida hasta que se completen todos los turnos disponibles de la 
semana. Cada llamado incluye: legajo paciente(P##), odontólogo(A/B) y tipo de prestación (1: Consulta, 
2: Arreglo, 3: Cirugía/Estética). Se debe realizar lo siguiente: 
a) Generar los vectores para representar los turnos asignados por odontólogo y por día. 
b) Verificar si hay tiempo suficiente para asignar el turno, en caso contrario asignarlo para el 
próximo turno día disponible.  
c) Mostrar: -Cantidad de turnos asignados por día. -Minutos restantes por día (deberían ser 0 en asignaciones de turno exitosas). -Total de prestaciones por tipo y odontólogo semanal."""

llamada=input("Hay una llamada entrante? si/no: ")[0].upper()
docA=[]
docB=[]
cl=300
cma=300
cmi=300
cj=300
cv=300
while llamada=="S":
    dia=input("ingrese dia: ").upper()
    consulta=input("Ingrese tipo de consulta").upper()
    b=0
    if dia=="LUNES":
        if consulta=="CIRUGIA" and cl>=90 and b==0:
            nombre=input("ingrese el nombre: ")
            apellido=input("ingrese apellido: ")
            dni=int(input("ingrese el dni: "))
            b=1
        if consulta=="ARREGLO" and cl>=60 and b==0:
            nombre=input("ingrese el nombre: ")
            apellido=input("ingrese apellido: ")
            dni=int(input("ingrese el dni: "))    
            b=1        
        if consulta=="CONSULTA" and cl>=30 and b==0:
            nombre=input("ingrese el nombre: ")
            apellido=input("ingrese apellido: ")
            dni=int(input("ingrese el dni: "))
            b=1
#mucho texto me aburrio