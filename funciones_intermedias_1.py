#Brandon Morales 
#19/04/2024

# funciones_intermedias_1.py

# 1. Actualizar valores en diccionarios y listas

# Cambiar valor en la matriz
matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6

# Cambiar nombre del primer cantante
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

# Cambiar "Cancún" por "Monterrey"
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"

# Cambiar latitud
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431

# Mostrar cambios
print("Matriz:", matriz)
print("Cantantes:", cantantes)
print("Ciudades:", ciudades)
print("Coordenadas:", coordenadas)


# 2. Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        linea = []
        for clave, valor in diccionario.items():
            linea.append(f"{clave} - {valor}")
        print(", ".join(linea))


# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])


# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
        print()  # línea en blanco entre secciones


# Ejemplos de uso:

# Lista extendida de cantantes
cantantes = [
    {"nombre": "Enrique Martin Morales", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

print("\n--- Iterar Diccionario ---")
iterarDiccionario(cantantes)

print("\n--- Iterar Diccionario 2 (nombre) ---")
iterarDiccionario2("nombre", cantantes)

print("\n--- Iterar Diccionario 2 (pais) ---")
iterarDiccionario2("pais", cantantes)

print("\n--- Imprimir Información ---")
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
imprimirInformacion(costa_rica)
