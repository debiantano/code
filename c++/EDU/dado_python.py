#!/usr/bin/python
import random

class Dado:
	def __init__(self, cantidadLados, ladoActual=0):
		self.ladoActual = ladoActual
		self.cantidadLados = cantidadLados

	def lanzar(self):
		self.ladoActual = random.randint(1,6)

	def obtenerLadoActual(self):
		if self.ladoActual==0:
			print("El dado NO se ha lanzado")
			return self.ladoActual
		else:
			return self.ladoActual

dado1 = Dado(6)
print("Creando dado")
dado1.lanzar()
print("Cara Actual: " + str(dado1.obtenerLadoActual()))
