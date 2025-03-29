# Creacion de diccionario nombre "informacion_personal"
informacion_personal = {
    "nombre": "Kevin Salazar",
    "edad": 19,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Ibarra"

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Ingeniero en tecnologias de la informacion"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "097-134-5664"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario finalizado
print(informacion_personal)
