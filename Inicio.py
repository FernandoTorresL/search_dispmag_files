import os
from operacionArchivos import *

ruta = 'C:\\dirA\\txt_files'
archivos = obtenNombreArchivos(ruta)

for registros in archivos:
	rutaArchivo = ruta + '\\' + registros
	rutaResultado = ruta + '\\res_' + registros
	resultado = concatenaRegistros(rutaArchivo,registros)
	guardaConcatenado(rutaResultado ,resultado)


