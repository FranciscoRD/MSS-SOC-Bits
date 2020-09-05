#!/usr/bin/env python3
import os
from sys import platform

termino = input("Ingrese termino: ").replace(" ","+")
ubicacion = input("Ingrese sitio: ")

buscador = f'http://www.google.com/search?q=intext:{termino}+inurl:{ubicacion}'

if platform == "linux" or platform == "linux2":
    print(buscador)
elif platform == "darwin":
    print("os x")
elif platform == "win32":
    busqueda = f'start {buscador}'

#Buscar en Linux
# busqueda = f'x-www-browser {buscador}'
# busqueda = f'xdg-open {buscador}'
# busqueda = f'gnome-open {buscador}'

#Si lynx esta instalado
#busqueda = f'lynx {buscador}'
#Buscar y guardar el resultado
#busqueda = f'lynx -source {buscador} > prueba.html'

# os.system(busqueda)
