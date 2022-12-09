import sys

argumentos=sys.argv

if len(argumentos)!=3:
    print("ERROR: debes ingresar dos argumentos")
    print("ejemplo: python script_argumentos2.py palabra cantidad")
else:
    palabra=argumentos[1]
    cantidad=int(argumentos[2])

    for i in range(cantidad)
        print(palabra)