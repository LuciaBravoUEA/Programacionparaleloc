# Crear una matriz bidimensional (3x3) con valores numéricos
matriz = [
    [5,  10, 15],
    [20, 25, 30],
    [35, 40, 45],
]
# Búsqueda de un valor específico en la matriz
valor_buscado = 25
if any(valor_buscado in fila for fila  in matriz):
    print(f"se encontró {valor_buscado} en la matriz.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
    