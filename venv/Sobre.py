from datetime import datetime

class Sobre:
    def __init__(self, nombre, descripcion, precio):
        self.Identificador = datetime.now()
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cartas = []

    def AñadirCartas(self, carta):
        self.cartas.append(carta)

    def veureCartesSobre(self):
        for item in range(len(self.cartas)):
            print("Nombre: " + self.cartas[item].nombre + " Tipo carta: " + self.cartas[item].tipo +" Rareza: " + self.cartas[item].rareza)