def temperatura_promedio(ciudades_temperaturas):

    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Creamos los parlamentos ciudades y temperaturas.
ciudades_temperaturas = {
    "SANGOLQUI": [19, 41, 9, 19, 33],
    "TUMBACO": [41, 10, 17, 29, 14],
    "CAYAMBE": [22, 8, 26, 33, 39],

}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f} °C")