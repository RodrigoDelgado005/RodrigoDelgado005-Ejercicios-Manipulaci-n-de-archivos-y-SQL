archivo = open("notas.txt", "x")
archivo.write("1. Programación: Me encanta resolver problemas lógicos y crear soluciones automatizadas.\n")
archivo.write("2. Redes: Es fascinante entender cómo los dispositivos se comunican entre sí.\n")
archivo.write("3. Inteligencia Artificial: Me interesa cómo las máquinas pueden aprender y tomar decisiones.\n")
archivo.close()
archivo = open("notas.txt", "r")

for linea in archivo:
    print(linea, end="") 

archivo.close()