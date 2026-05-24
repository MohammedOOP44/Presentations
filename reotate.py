from PIL import Image , ImageOps 

img = Image.open("example.png")
bordered = ImageOps.expand(img,border=10,fill="white")
bordered.save("output.burder.png")
bordered.show()
