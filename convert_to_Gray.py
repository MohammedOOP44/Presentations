from PIL import Image , ImageOps

img = Image.open("example.png")
gray = ImageOps.grayscale(img)
gray.save("output_grayscale.png")

gray.show()