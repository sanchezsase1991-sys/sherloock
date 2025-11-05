from sherloock import sherloock

# Instancia con mayor potencia de hilos lógicos
ia = sherloock.Sherloock(max_fibers=8)

# Definir reglas personalizadas
ia.add_rule(r"energía", "La energía no se crea ni se destruye.")
ia.add_rule(r"pi", "π ≈ 3.1415926535, constante fundamental.")

# Probar razonamiento híbrido
print(ia.reason("energía"))
print(ia.reason("forecast [30, 42, 55, 67] with_limit avg*1.2"))

# Resolver lógica simbólica compleja
print(ia.reason("logic Eq(x**2 - 4, 0)"))

# Ejecución paralela simbólica
print(ia.reason("solve parallel pitagoras"))
