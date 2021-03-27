import os

def obtenNombreArchivos(ruta):

	archivos = list()
	with os.scandir(ruta) as ficheros:
		for fichero in ficheros:
			archivos.append(fichero.name)
	return archivos


def concatenaRegistros(ruta,nombreArchivo):
	registroConcatenado = list()

	with open(ruta,'r') as lecturaArchivo:
		for registro in lecturaArchivo:
			registroConcatenado.append(registro.rstrip('\n')+nombreArchivo)
	return(registroConcatenado)


def guardaConcatenado(ruta,resultado):

	ArchivoResultado = open(ruta,'a')
	for registro in resultado:
		if registro is not None:
			ArchivoResultado.write(str(registro)+ '\n' )
			# print(str(registro)+ '\n')
	ArchivoResultado.close()
