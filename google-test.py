#!/usr/bin/env python3
import os

termino = 'Pete+Treperinas+Maven'
ubicacion = 'linkedin.com'

buscador = f'http://www.google.com/search?q=intext:{termino}+inurl:{ubicacion}'

#Buscar en windows
busqueda = f'start {buscador}'

#Buscar en Linux
# busqueda = f'x-www-browser {buscador}'

#Buscar en Linux
# busqueda = f'xdg-open {buscador}'

#Buscar en Linux
# busqueda = f'gnome-open {buscador}'

#Si lynx esta instalado
#busqueda = f'lynx {buscador}'
#Buscar y guardar el resultado
#busqueda = f'lynx -source {buscador} > prueba.html'

os.system(busqueda)
