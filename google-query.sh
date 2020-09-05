#!/bin/bash

echo Bienvenido al script de google dorks

echo A que persona u organizacion desea buscar
read persona

echo En que sitio desea buscarla?
read sitio

echo buscando a $persona en $sitio

x-www-browser http://www.google.com/search?q=intext:$persona%20inurl:$sitio

wget --user-agent="Mozilla" http://www.google.com/search?q=intext:$persona%20inurl:$sitio
