from PIL import Image , ImageOps 

img = Image.open("ex.png")

bordered = ImageOps.expand(img,border=10,fill='red')
bordered.save("output_border1.png")
