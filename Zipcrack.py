#Zip File Brutforce
import zipfile
import itertools
import string
from threading import Thread

def crack (zip, pwd):
    try:
        zip.extractall (pwd=str.encode(pwd))
        print ("Success:"+pwd)
    except:
        pass

zipFile= zipfile.ZipFile("C:\\Users\\Sumeronix\\Documents\\loesungen.zip")
myLetters= string.ascii_letters + string.digits + string.punctuation
for i in range (3,10):
    for j in map ("".join, itertools.product(myLetters, repeat=i)):
        t= Thread(target=crack,args=(zipFile,j))
        t.start()

