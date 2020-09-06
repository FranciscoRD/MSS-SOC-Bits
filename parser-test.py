import os
import csv

def procesar():
    archivo = "online-valid.csv"
    campos = []
    elementos = [] 

    with open(archivo, 'r') as csvfile: 
	    csvreader = csv.reader(csvfile) 
	    campos = next(csvreader) 
	    for row in csvreader:
    		elementos.append(row)  
	    print("Numero total de filas: %d"%(csvreader.line_num))

    print('Nombre de Campos:' + ', '.join(campo for campo in campos)) 

    print('\nPrimeros 2 elementos:\n') 
    for row in elementos[:2]: 
	    for col in row: 
		    print(col), 
	    print('\n') 

if os.path.isfile('online-valid.csv'):
    procesar()
else:
    os.system('wget http://data.phishtank.com/data/online-valid.csv')
    (columnas,filas) = os.get_terminal_size()
    print('\n')
    print('='*columnas)
    procesar()
