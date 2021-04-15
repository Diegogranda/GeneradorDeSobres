from Cartas import Cartas
from Sobre import Sobre

c1 = Cartas("Goku ","ss4","Rara",99,80,95,"Puñetazo")
c2 = Cartas("Picolo","ss2","Muy Rara",99,80,95,"Patada voladora")
s1 = Sobre("Sobre Premium","100.000€",1)
s1.AñadirCartas(c1)
s1.AñadirCartas(c2)
s1.veureCartesSobre()