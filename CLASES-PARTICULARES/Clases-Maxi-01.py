# a) Cargar un vector inicial con los tipos de eventos válidos
eventos_validos = []
print("--- Carga de eventos válidos ---")
evento = input("Ingrese tipo de evento válido (FIN para terminar): ")

while evento != "FIN":
    # Búsqueda secuencial manual para verificar si ya existe
    encontrado = False
    indice = 0
    while indice < len(eventos_validos) and encontrado == False:
        if eventos_validos[indice] == evento:
            encontrado = True
        indice += 1
        
    if encontrado == False:
        eventos_validos.append(evento)
    else:
        print("El evento ya fue ingresado.")
        
    evento = input("Ingrese tipo de evento válido (FIN para terminar): ")

# b) Cargar eventos y horas en un nuevo vector
registro_eventos = []
print("\n--- Carga de registro de eventos ---")
evento_ingresado = input("Ingrese evento (FIN para terminar): ")

while evento_ingresado != "FIN":
    # Búsqueda secuencial manual para validar que el evento exista en el vector inicial
    es_valido = False
    k = 0
    while k < len(eventos_validos) and es_valido == False:
        if eventos_validos[k] == evento_ingresado:
            es_valido = True
        k += 1
    if es_valido == False:
        print('Mensaje: "Falla no es un evento válido, ingrese nuevamente!"')
    else:
        hora = input("Ingrese hora: ")
        
        # Buscar la posición para insertar al final del grupo correspondiente[cite: 1]
        i = len(registro_eventos) - 2
        posicion_insertar = len(registro_eventos)
        insertado = False
        
        # Recorremos el vector de atrás hacia adelante buscando el evento[cite: 1]
        while i >= 0 and insertado == False:
            if registro_eventos[i] == evento_ingresado:
                posicion_insertar = i + 2
                insertado = True
            i -= 2
        # Insertar el evento y su hora manteniendo el orden[cite: 1]
        registro_eventos.insert(posicion_insertar, evento_ingresado)
        registro_eventos.insert(posicion_insertar + 1, hora)
                    
        print("-> Vector:", registro_eventos)
            
    evento_ingresado = input("Ingrese evento (FIN para terminar): ")
"""
Por defecto, si aún no existe, va al final del vector B[cite: 1]
    posicion_insertar = len(B)
        
# Recorremos solo los índices pares (donde están los nombres de los eventos)[cite: 1]
for i in range(0, len(B), 2):
    if B[i] == evento_ingresado:
        # Cada vez que lo encuentra, actualiza la posición al final de ese grupo[cite: 1]
        posicion_insertar = i + 2
        
    # Insertar el evento y su hora manteniendo el orden en B[cite: 1]
B.insert(posicion_insertar, evento_ingresado)
B.insert(posicion_insertar + 1, hora)        
    print("-> Vector:", B)
    for i in range (len(B))
        print("los elemenos son:",B[i])
evento_ingresado = input("Ingrese evento (FIN para terminar): ")
"""
# c) Determinar el evento con mayor secuencia[cite: 1]
# d) Mostrar la cantidad de veces que aparece cada tipo de evento[cite: 1]
print("\n--- Resultados ---")
evento_mayor_secuencia = ""
mayor_cantidad = 0
salida_d = ""

i = 0
while i < len(eventos_validos):
    evento_actual = eventos_validos[i]
    cantidad_actual = 0
    
    # Contar cuántas veces aparece evento_actual en el registro
    j = 0
    while j < len(registro_eventos):
        if registro_eventos[j] == evento_actual:
            cantidad_actual += 1
        j += 2
        
    # Actualizar la mayor secuencia
    if cantidad_actual > mayor_cantidad:
        mayor_cantidad = cantidad_actual
        evento_mayor_secuencia = evento_actual
        
    # Formatear la cadena de salida para el inciso d[cite: 1]
    if i > 0:
        if i == len(eventos_validos) - 1:
            salida_d += " y "
        else:
            salida_d += ", "
    salida_d += '"' + evento_actual + '": ' + str(cantidad_actual)
        
    i += 1

print('c) El evento con mayor frecuencia es "' + evento_mayor_secuencia + '" con ' + str(mayor_cantidad) + ' ocurrencias.')
print('d)', salida_d)
"""print("\n--- Resultados ---")
evento_mayor_secuencia = ""
mayor_cantidad = 0
salida_d = ""

for i in range(len(eventos_validos)):
    evento_actual = eventos_validos[i]
    cantidad_actual = 0
    
    # Contar con for cuántas veces aparece evento_actual en B (saltando de a 2)[cite: 1]
    for j in range(0, len(B), 2):
        if B[j] == evento_actual:
            cantidad_actual += 1
            
    # Actualizar la mayor cantidad
    if cantidad_actual > mayor_cantidad:
        mayor_cantidad = cantidad_actual
        evento_mayor_secuencia = evento_actual
        
    # Formatear la cadena de salida para el inciso d[cite: 1]
    print("el mayor evento es":evento_mayor_secuencia,"y la frecuencia es)
"""