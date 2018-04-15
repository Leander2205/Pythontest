#Sets Mengen
familie_mutter = {"Jochen","Klaus","Peter"}
familie_vater = {"Klaus","Jochen","Anne"}
#Ist Element in einer Menge
print ("dieter" in familie_mutter)
print ("dieter" in familie_vater)

# Vereinigungsmenge | (oder)
familie = familie_mutter| familie_vater
print(familie)
# Was liegt in beiden Mengen (und)
print (familie_mutter&familie_vater)
# A ohne B
print (familie_mutter-familie_vater)

#Sortieren
import random
data = [random.randint (0,100) for _ in range (10)]
print (data)
#wird in alter Liste gespeichert
data.sort ()
print (data)
# neue Liste wird erstellt
data2 = sorted (data)
print (data2)
#aufsteigend absteigend sorted (data,reverse=false) oder data.sort (reverse= true)
#sorted kann auf alles angewendet werden was itterierbar
name = "Leander"
sortiert = sorted(name)
print (sortiert)
#Funktionen erstellen definieren und aufrufen
def func (a,b=None):
    print ("test")
    return a * b
wert= func (1,2)
print (wert)
#Module laden und eigene (mean= Mittelwert)
import numpy
import numpy as np
print (numpy.mean ([1,2]))
#Nur einzelne Funktionen eines Moduls laden
from numpy import mean
print (mean ([1,2]))
#Eigenes Modul laden
import Modul
val , a, b = Modul.func ()
print (val)



