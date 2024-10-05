
#Abre el archivo my_notes.txt.
"""file = open("my_notes.txt" , "r")
#print(file)
lineas = file.readlines()
print(lineas)
# Asegúrate de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
file.close()"""


#definimos el nombre del archivo
file_name = "my_notes.txt"

#Abrimos el archivo "w" pqara la escritura write
archivo_datos = open(file_name, "w")
# metodo write()
archivo_datos.write("Linea 1: Lucia Cristina.\n")
archivo_datos.write("Linea 2: Bravo Ostaiza.\n")
archivo_datos.write("Linea 3: Vivo en Sucumbios.\n")
archivo_datos.write("Linea 4: Lago Agrio.\n")
archivo_datos.write("Linea 5: Soy Estudiante.\n")
print(archivo_datos)
#Cerramos el archivo
archivo_datos.close()

# modo de apertura "r" para lectura
archivo_datos = open(file_name, "r")
#Metodo read():lee  todo el contenido del archivo
contenido_completo = archivo_datos.read()
print("contenido completo usando read():")
print(contenido_completo)

#Metodo readline():leer una linea a la vez
archivo_datos.seek(0)                    #reiniciamos al cursor al principio del archivo
linea_1 = archivo_datos.readline()
linea_2 = archivo_datos.readline()
linea_3 = archivo_datos.readline()
linea_4 = archivo_datos.readline()
linea_5 = archivo_datos.readline()
#Imprimir las lineas
print("\ncontenido linea por linea usando readline():")
print("linea_1:" , linea_1.strip())  # strip() elimina el salto de linea
print("linea_2:" , linea_2.strip())
print("linea_3:" , linea_3.strip())
print("linea_4:" , linea_4.strip())
print("linea_5:" , linea_5.strip())


