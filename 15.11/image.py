from PIL import Image

def bilde():

  datne = "15.11/R.jpeg"

  with Image.open(datne) as im:
    print(datne, im.format , f"{im.size}x{im.mode}")
    im.show()
    izmers = (50,50)
    im.thumbnail(izmers)
    im.save("maza_bilde.jpg", im.format)
    im.show()

bilde()

im = Image.open("15.11/R.jpeg")


angle = 90

out = im.rotate(angle)
out.save('rotate-output.png')


