from PIL import Image

img = Image.open("example.png")
resize = img.resize((1000,1000))
resize.save("new_size.png")
resize.show()