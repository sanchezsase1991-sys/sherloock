from .Sherloock import sherloock   # CORRECTO según tu estructura

bot = Sherloock()

print("Sherlook – Escribe 'quit' para salir")
while True:
    cmd = input("Sherlook> ")
    if cmd.lower() in ["exit", "quit"]:
        break
    print(bot.reason(cmd))
