#Crear un programa en esta hoja que reciba un numero cualquiera por consola, guarde el numero en una variable 
#e imprima todos los numero pares que hay entre 0 y el numero dado por consola
#por ejemplo si recibimos 10  el programa tendra que imprimir 2 4 6 8 .
#si le damos 15 tendra que imprimir 2 4 6 8 10 12 14
#si le damos 1 no imprimira nada y asi sucesivamente
#Buscar en google como saber si un numero es par"
z=int(input("ingresar numero: "))
print(f"Números pares entre 0 y {z} son:")
for i in range(z+1):
    if i %2==0:print(i)