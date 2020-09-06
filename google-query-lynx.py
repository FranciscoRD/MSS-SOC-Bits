#!/usr/bin/env python3
import os
from sys import platform

def Lynx(busqueda):
    buscador = f'lynx -source {busqueda} > prueba.html'
    os.system(buscador)
    buscador = f'lynx {busqueda}'
    os.system(buscador)

def Mensaje():
    print('Tipos de Busquedas permitidas:')
    print('1. Busqueda simple')
    print('2. Busqueda por "site:"')
    print('3. Busqueda por "inurl:"')
    print('4. Busqueda por "intitle:"')
    print('5. Busqueda por "intext:')
    print('6. Busqueda por "filetype:"')


def Query():
    Mensaje()
    respuesta = input("Ingrese opcion: ").lower()

    if respuesta == '1':
        termino = input("Ingrese el termino: ").replace(" ","+")
        busqueda = f'http://www.google.com/search?q="{termino}"'
        Lynx(busqueda)
    elif respuesta == '2':
        termino = input("Ingrese el termino: ").replace(" ","+")
        parametro = input("Ingrese sitio: ")
        dork = f'site:{parametro}+'
        busqueda =f'http://www.google.com/search?q={dork}"{termino}"'
        Lynx(busqueda)
    elif respuesta == '3':
        termino = input("Ingrese el termino: ").replace(" ","+")
        busqueda =f'http://www.google.com/search?q=inurl:"{termino}"'
        Lynx(busqueda)
    elif respuesta == '4':
        termino = input("Ingrese el termino: ").replace(" ","+")
        parametro = input("Ingrese el titulo: ")
        dork = f'intitle:"{parametro}"+'
        busqueda =f'http://www.google.com/search?q={dork}"{termino}"'
        Lynx(busqueda)
    elif respuesta == '5':
        termino = input("Ingrese el termino: ").replace(" ","+")
        busqueda =f'http://www.google.com/search?q=intext:"{termino}"'
        Lynx(busqueda)
    elif respuesta == '6':
        termino = input("Ingrese el termino: ").replace(" ","+")
        parametro = input("Ingrese extencion de archivo: ")
        dork = f'filetype:{parametro}+'
        busqueda =f'http://www.google.com/search?q={dork}"{termino}"'
        Lynx(busqueda)
    else:
        print('Elemento incorrecto')


def Inicio():
    print('Gestor de Consultas de Google')
    print('Adertencia este programa hace uso del navegador de texto "LYNX" ')
    print('para ver y guardar las consultas hechas')
    continuar = input('Desea continuar con el programa (N/n para salir, cualquier tecla para continuar): ').lower()
    while continuar != 'n':
        Query()
        continuar = input('Desea continuar con el programa (N/n para salir, cualquier tecla para continuar): ').lower()
    print('Adios')


Inicio()
