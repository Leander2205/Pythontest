class Menschen:
    Name =""
    Nachname =""
    Alter = 0
def __init__ (self,Name,Nachname,Alter):
   self.Name = Name
   self.Nachname = Nachname
   self.Alter = Alter
def print_daten(self):
    print ("Mensch:",self.name,"",self.nachname,"Alter",self.alter)

class Student (Mensch):
    mnr= 0
    semester = 0
    studiengang = ""    
    
    def __init__(self,mnr,semester,studiengang,Name,Nachname,Alter)
        super (Student, self).__init__(Name,Nachname,Alter)
        self.mnr = mnr
        self.semester = semester
        self.studiengang= studiengang