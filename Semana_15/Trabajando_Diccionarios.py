#Crea un diccionario llamado informacion_personal que contenga información ficticia
# sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
#Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un
# número de teléfono ficticio.
#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.

# 1 creamos el diccionario

"""
informacion_personal = {"nombre": "Monica", "edad": "28", "ciudad": "Loja", "profesion": "Enfermera"}

# Accede el valor asociado con la clave "cuidad" y modificar con una diferente
informacion_personal["ciudad"] = "Cayambe"

#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
informacion_personal["profesion_segura"] = "Enfermera general"

#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un
# número de teléfono ficticio.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0989949474"

#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal["edad"]
print(informacion_personal)
  """


while True:
    datos_personales=input("Ingrese el nombre")
    edad=int(input("Ingrese la edad"))
    ciudad=float(input("Ingrese la ciudad"))

    informacion_personal = {datos_personales, edad,ciudad}

    ingrese = int(input("para terminar digite 0"))
    if ingrese == 0:
        break;

    print(informacion_personal)



