from PIL import Image, ExifTags
#Dateipfad in Klammer
img = Image.open ("C:\\Users\\Sumeronix\\Desktop\\image.jpeg")
for i,j in img._getexif().items():
    if i in ExifTags.TAGS:
        print (ExifTags.TAGS[i]+ "-"+str(j))
