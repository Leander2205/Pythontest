#Eigene Klassen erstellen   Self und init Funktion müssen definiert werden
class Vector3d:
    x = 0
    y = 0
    z = 0

#Konstruktor
    def __init__ (self, x=0, y=0,z=0):
        self.x = x
        self.y = y
        self.z =z
    def printCoordinates (self):
        print ("x:",self.x)
        print ("y:",self.y)
        print ("z:",self.z)
null_vector= Vector3d(0,0,0)
null_vector.printCoordinates()  

v1= Vector3d(2,3,4)
v1.printCoordinates()
 #Vererbung von Klassen
class Tier:
    rasse = ""
    geschlecht = ""
    alter = 0

    def __init__ (self, rasse, geschlecht, alter):
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printRasse(self):
        print ("(Tier) Rasse:", self.rasse)
class Hund (Tier):
    tatzen = 0

    def __init__ (self,tatzen,rasse,geschlecht,alter):
        super(Hund,self).__init__(rasse,geschlecht,alter)