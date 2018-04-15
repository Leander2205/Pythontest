#Dateien lesen und schreiben
text = "Heute ist  ein schöner Tag"
text2 = "Was ein drecks Wetter"
data = [1,3,5,7,8,9]
# w=schreiben,r=lesen,a= append
# with open (dateiname,modus) as fileObject:
with open ("Geschichte.txt","w") as f:
    f.write(text+"\n")
    f.write(text2+"\n")
#Lesen von Dateien (Readlines benutzt immer strings) wenn man mit zahlen rechnen
# will muss man diese erst wieder casten (val(str))
text_neu = ""
with open ("Geschichte.txt","r") as f:
    text_neu = f.readlines()
    for line in f:
        print(line)
        text_neu += line
print (text_neu)

with open ("data.txt","a") as f:
    for val in data:
        f.write (str(val)+",")