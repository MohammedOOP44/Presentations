from PIL import Image , ImageOps

img = Image.open("ex.png")

gray = ImageOps.grayscale(img)
gray.save("output_grayscale1.png")

