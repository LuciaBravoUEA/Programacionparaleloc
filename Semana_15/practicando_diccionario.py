#Creamos el diccionario
datos_personales = []
#una funcion
def agregar_informacion_personal(nombre, edad, ciudad):
    informacion_personal = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }
    datos_personales.append(informacion_personal)

#Agregamos datos
agregar_informacion_personal("Julio", 35,"Ambato")
agregar_informacion_personal("Maria", 29, "Cayambe")
agregar_informacion_personal("Lorena", 22, "Quito")
agregar_informacion_personal("Moises", 20, "Manabi")

print(datos_personales)