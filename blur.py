from PIL import Image , ImageFilter

img = Image.open("ex.png")
blurred = img.filter(ImageFilter.BLUR)
blurred.save("output_blure.png")