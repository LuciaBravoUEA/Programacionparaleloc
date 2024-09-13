
arreglo_temperaturas = [
  [#RIOBAMBA
    [1,2,3,4,5,6,7],
    [35, 45, 19, 28, 38, 10, 17]
  ],
  [# MANTA
    [1, 2, 3, 4, 5, 6, 7],
    [9, 41, 29, 15, 17, 20, 8]
  ],
  [#MANABI
    [1, 2, 3, 4, 5, 6, 7],
    [33, 45, 26, 17, 38, 21, 8]
  ],
  [#QUITO
    [1, 2, 3, 4, 5, 6, 7],
    [11, 25, 36, 39, 28, 9, 14]
  ],
]

def temperatura_promedio(arreglo_temperaturas,ciudad, semana):
  total=0
  for i in range (len (arreglo_temperaturas[ciudad][semana])):
    total = total + arreglo_temperaturas[ciudad][semana][i]

  promedio = total / len(arreglo_temperaturas[ciudad][semana])

  return promedio

resultado_promedio = temperatura_promedio(arreglo_temperaturas,0,1)

print(resultado_promedio)


