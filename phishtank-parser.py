import os
import csv

def Procesar():
    archivo = "online-valid.csv"
    campos = []
    elementos = [] 

    with open(archivo, 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        campos = next(csvreader) 
        for row in csvreader:
            elementos.append(row)
        print("Numero total de registros: %d"%(csvreader.line_num))

    print('Nombre de Campos:' + ', '.join(campo for campo in campos)) 

    mostrar = int(input(f'Cuantos registros quiere ver ( 1 - {csvreader.line_num}) ?: '))
    for row in elementos[:mostrar]:
        print("="*20)
        for col in row: 
            print(col), 
    print('\n')


if os.path.isfile('online-valid.csv'):
    Procesar()
else:
    os.system('wget http://data.phishtank.com/data/online-valid.csv')
    (columnas,filas) = os.get_terminal_size()
    print('\n')
    print('='*columnas)
    Procesar()
