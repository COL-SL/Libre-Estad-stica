# Modulo coche.py
# !/usr/bin/env python

class Coche:
    def __init__(self, velocidad, nombre, temperatura):
        self.velocidad = velocidad
        self.nombre = nombre
        self.temperatura = temperatura

    def acelerar(self):
        self.velocidad += 1
        print 'La velocidad actual es de ', self.velocidad

    def frenar(self):
        if self.velocidad == 0:
            print 'El carro se ha detenido'
        else:
            self.velocidad -= 1
            print 'La velocidad actual es de ', self.velocidad
