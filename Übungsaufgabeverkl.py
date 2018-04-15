class Mensch:
    name = ""
    nachname = ""
    alter = 0

    def __init__(self, name, nachname, alter):
        self.name = name
        self.nachname = nachname
        self.alter = alter

    def print_daten(self):
        print('Mensch: ', self.name, " ", self.nachname, " Alter: ", self.alter)

class Student(Mensch):
    mnr = 0
    semester = 0
    studiengang = ""

    def __init__(self, mnr, semester, studiengang, name, nachname, alter):
        super(Student, self).__init__(name, nachname, alter)
        self.mnr = mnr
        self.semester = semester
        self.studiengang = studiengang

    def print_daten(self):
        super(Student, self).print_daten()
        print('Mnr: ', self.mnr, ' Semester: ', self.semester, ' Studiengang: ', self.studiengang)
Leander = Student(256654,4,"BachelorScience","Leander","R",19)
Leander.print_daten()
#Ist Leander eine Instanz der Klasse Student?
peter = Mensch("Peter","H",54)
print("Ist Leander ein Student?")
if isinstance(Leander,Student):
    print("Ja")
else:
    print ("Nein")