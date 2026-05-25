from PIL import Image 

img = Image.open("ex.png")

rotated = img.rotate(60)
rotated.save("output_rotate.png")