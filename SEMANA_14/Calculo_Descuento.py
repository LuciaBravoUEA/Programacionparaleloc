#Definimos la función calcular_descuento
def calcular_descuento(valor_total,aplicar_descuento=20):
    descuento = (valor_total * aplicar_descuento) / 100
    return descuento

#parametros
valor_1 = 530
valor_2 = 780
valor_3 = 489
valor_4 = 295
aplicar_descuento1 = 18
aplicar_descuento4 = 20

#Llamamos a la función
descuento1 = calcular_descuento(valor_1)
descuento2 = calcular_descuento(valor_2, aplicar_descuento1)
descuento3 = calcular_descuento(valor_3, aplicar_descuento4)

# Mostrar los resultados
print(f"compra 1: valor total = {valor_1}, descuento = {descuento1} total = {valor_1 - descuento1}")
print(f"compra 2: valor total = {valor_2}, descuento = {descuento2} total = {valor_2 - descuento2}")
print(f"compra 3: valor total = {valor_3}, descuento = {descuento3} total = {valor_3 - descuento3}")


