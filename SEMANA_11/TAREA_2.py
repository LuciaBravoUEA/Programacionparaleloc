# Crear una matriz bidimencional de (3x3)  con valores numéricos
matriz=[
    [40, 41, 42],
    [43, 44, 45],
    [46, 47, 48]
]
# Valor que estamos buscando
valor_buscado= 48

# Iniciar variable para rastrar la posición del valor
fila_encontrada = -2
columna_encontrada = -2

# Recorrer la matriz para buscar el valor
for fila in  range (len (matriz)):
    for columna in range (len (matriz[fila])):
        if matriz [fila][columna]== valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
# salir del bucle exterior si se encuentra el valor


# Verificar si se encontro el valor y mostrar la posición

if fila_encontrada != - 2 :
    print (f"se encontró {valor_buscado } en la fila { fila_encontrada } y columna { columna_encontrada} . ")
else:
    print (f"se encontró {valor_buscado } no se encontró en la matriz." )
