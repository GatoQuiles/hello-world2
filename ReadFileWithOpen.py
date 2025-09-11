#Crear un archivo con extension txt y abrirlo con with open 
#https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
archivo=open("archivo11.txt","x")
archivo=open("archivo11.txt","w")
A=["Acagar quijote \n","que paso \n"]
archivo.writelines(A)
with open("archivo11.txt") as archivo:
    print(archivo.read())