from sherloock import sherloock

# Crear instancia
ia = sherloock.Sherloock()

# Ejemplo básico: agregar una regla y razonar
ia.add_rule(r"hola", "¡Hola humano, soy Sherloock!")

print(ia.reason("hola"))
print(ia.reason("forecast [10, 15, 20]"))
print(ia.reason("logic x + 2 - 4"))
