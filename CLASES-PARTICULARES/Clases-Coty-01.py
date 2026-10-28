# BLOQUE 1: Carga de antenas válidas
antena_valida= []
print("--- Carga de antenas válidas ---")
antena = input("Ingrese tipo de antena válido (FIN para terminar): ")

while antena != "FIN":
    # Búsqueda secuencial manual para verificar si ya existe
    encontrado = False
    indice = 0
    while indice < len(antena_valida) and encontrado == False:
        if antena_valida[indice] == antena:
            encontrado = True
        indice += 1
    if encontrado == False:
        antena_valida.append(antena)
    else:
        print("La antena ya fue ingresado.")
        
    antena = input("Ingrese tipo de antena válido (FIN para terminar): ")
    
"""Qué hace: Crea un vector inicial sin elementos repetidos que servirá como validación para el resto del programa.Cómo funciona: Utiliza un ciclo while controlado por un valor de corte ("FIN"). Por cada antena ingresada, hace una búsqueda secuencial manual en el vector antena_valida. Si la bandera encontrado sigue siendo False al terminar de revisar, lo agrega; si no, avisa que está repetido.Posibles errores que hay que evitar en el parcial:
Bucle infinito: Olvidarse de volver a pedir el input de antena justo antes de que termine el while.
Confusión de mayúsculas/minúsculas: Si el alumno escribe "fin" en minúscula, el programa no cortará. (Para primer año alcanza con avisarles que escriban siempre en mayúscula)."""
# BLOQUE 2: Carga de datos en el Vector B
B=[]#el vector de enventos
antena = input("Ingrese antenas (FIN para terminar): ")
while antena != "FIN": 
    posicion_insertar = len(B)
    es_valido = False
    k = 0
    while k < len(antena_valida) and es_valido == False:
        if antena_valida[k] == antena:
            es_valido = True
        k += 1
    if es_valido == False:
        print('Mensaje: "Falla no es una antena no válida, ingrese nuevamente!"')
    else:
        codigo = input("Ingrese codigo: ") 
        # Recorremos solo los índices pares (donde están los nombres de los eventos)[cite: 1]
        for i in range(0, len(B), 2):
            if B[i] == antena_valida:
                # Cada vez que lo encuentra, actualiza la posición al final de ese grupo[cite: 1]
                posicion_insertar = i + 2
        
        # Insertar el evento y su hora manteniendo el orden en B[cite: 1]
        B.insert(posicion_insertar, antena_valida)
        B.insert(posicion_insertar + 1, codigo)
    antena= input("Ingrese antenas (FIN para terminar): ")

for i in range (len(B)):
    print("los elemenos son:",B[i])
"""Qué hace: Carga las antenas y sus códigos en el vector B, validando que la antena exista y agrupando los datos para que las antenas iguales queden juntas.Cómo funciona: Primero verifica secuencialmente si la antena ingresada está en el vector antena_valida. Si lo está, pide el código. Luego, recorre los índices pares de B buscando si esa antena ya se ingresó antes. Si la encuentra, actualiza la posicion_insertar para colocar el nuevo dato justo después de ese grupo.Posibles errores que hay que evitar en el parcial (Errores graves que tenías en tu código original):
Comparar e insertar listas enteras en lugar de strings: En tu código original tenías if B[i] == antena_valida: y B.insert(posicion_insertar, antena_valida). antena_valida es el vector completo (lista). Deben comparar e insertar la variable string antena.
Falta de lectura al final del ciclo: En tu código faltaba el input al final del while, lo que generaba un bucle infinito en cuanto ingresaban una antena válida."""
# BLOQUE 3: Determinar el código con mayor secuencia
print("\n--- Resultados ---")
codigo_mayor_secuencia = ""
codigo_cantidad = 0

for i in range(1,len(B),2):
    codigo_actual = B[i]
    cantidad_actual = 0
    
    # Contar con for cuántas veces aparece antena_actual en B (saltando de a 2)
    for j in range(1, len(B), 2):
        if B[j] == codigo_actual:#B[j]==B[i]
            cantidad_actual += 1
            
    # Actualizar la mayor cantidad
    if cantidad_actual > codigo_cantidad:
        codigo_cantidad = cantidad_actual
        codigo_mayor_secuencia = codigo_actual
        
    # Formatear la cadena de salida para el inciso d[cite: 1]
print("El codigo:",codigo_mayor_secuencia,"es el mas frecuente, sale:",codigo_cantidad,"veces")
"""Qué hace: Busca cuál es el "código" (no la antena) que más veces se repite en todo el vector B.Cómo funciona: Utiliza dos ciclos for anidados que recorren únicamente las posiciones impares range(1, len(B), 2), que es donde se guardaron los códigos. Toma un código, lo compara contra todos los demás, cuenta las coincidencias y guarda el máximo.Posibles errores que hay que evitar en el parcial:
Imprimir las variables al revés: En tu código original decía El codigo: [cantidad] ... sale: [nombre] veces. Hay que prestar atención al orden en los print.
Arrancar en el índice equivocado: Como los códigos están en las posiciones 1, 3, 5, etc., es vital que el range empiece en 1 y salte de a 2. Si empiezan en 0, van a contar las antenas."""
# BLOQUE 4: Frecuencia de cada antena
con=0
for k in range(len(B)):
    for i in range(0,len(B),2):
        if B[k]==B[i]:
            con+=1
    print("La antena mas frecuente es:",B[i],"con una frecuencia de:",con)
"""Qué hace: Muestra un listado de todas las antenas válidas y cuántas veces aparecieron en los eventos ingresados.Cómo funciona: Toma cada elemento del vector original antena_valida y lo busca en las posiciones pares del vector B range(0, len(B), 2). Cuenta las apariciones y las imprime.Posibles errores que hay que evitar en el parcial (Tu lógica original estaba rota aquí):
No resetear el contador: Es obligatorio que la variable acumuladora/contadora (con = 0) se ponga a cero adentro del primer ciclo, justo antes de empezar a contar una nueva antena. Si la ponen afuera, los números se van a sumar arrastrando los valores de la antena anterior.
Recorrer mal los vectores para contar: En tu código original hacías un for k in range(len(B)) y adentro otro for sobre B. Eso compara todo contra todo, imprime decenas de veces y cuenta mal. La forma correcta en algoritmos de primer año es iterar sobre el vector de "categorías únicas" (antena_valida) y contar sobre el vector de "registros" (B)."""