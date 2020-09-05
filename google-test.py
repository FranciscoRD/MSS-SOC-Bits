import os

termino = 'loana+lopez+gonzales'
ubicacion = 'linkedin.com'
buscador = f'http://www.google.com/search?q=intext:{termino}+inurl:{ubicacion}'
busqueda = f'start {buscador}'
os.system(busqueda)
