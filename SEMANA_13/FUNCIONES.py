#calcurar los promedios de las ciudades
arreglo_temperaturas = [
  [#RIOBAMBA
    [10, 19, 25, 19, 9, 78, 35],
    [35, 45, 19, 28, 38, 10, 17],
    [28, 29, 19, 33, 36, 22, 36],
    [11, 25, 36, 39, 28, 9, 14]
  ],
  [# MANTA
    [14, 11, 13, 5, 14, 17, 20],
    [9, 41, 29, 15, 17, 20, 8],
    [23, 25, 45, 38, 44, 42, 29],
    [7, 9, 16, 19, 25, 35, 30]
  ],
  [#MANABI
    [40, 36, 29, 19, 48, 39, 21],
    [33, 45, 26, 17, 38, 21, 8],
    [8, 26, 38, 45, 46, 23, 41],
    [23, 41, 31, 9, 10, 14, 29]

  ],
  [#QUITO
    [11, 25, 33, 42, 8, 26, 14],
    [11, 25, 36, 39, 28, 9, 14],
    [33, 41, 26, 32, 30, 29, 11],
    [33, 45, 26, 17, 38, 21, 8]
  ],
]
# calcular el promedio de una ciudad
def temperatura_promedio(arreglo_temperaturas,ciudad, semana):
  total=0
  for i in range (len (arreglo_temperaturas[ciudad][semana])):
    total = total + arreglo_temperaturas[ciudad][semana][i]

  promedio = total / len(arreglo_temperaturas[ciudad][semana])

  return promedio

resultado_promedio = temperatura_promedio(arreglo_temperaturas,0,1)

print(resultado_promedio)
# interactua calculando los promedios de las diferentes ciudades
resultado_promedio = temperatura_promedio(arreglo_temperaturas,1,2)

print(resultado_promedio)

resultado_promedio = temperatura_promedio(arreglo_temperaturas,2,3)

print(resultado_promedio)

resultado_promedio = temperatura_promedio(arreglo_temperaturas,3,3)

print(resultado_promedio)