archivo = open("miarchivo.txt", "x")
contenido = archivo.write("Hola, estoy aprendiendo python")
archivo.close()
archivo = open("miarchivo.txt", "r")
print(archivo.readline())
archivo.close()