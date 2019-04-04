# print("Hola Michel")
# print("Jimmy Calderon")

def gritar(frase):
    print(frase.upper())

saludo = input("Que queres repitir?\n")
veces = input("Cuantas veces lo repito?\n")
grtr = input("Queres gritar (si/no)?\n")
for i in range(int(veces)):
    if(grtr=='si'):
        gritar(saludo)
    else:
        print(saludo)

gritar("terminamos")