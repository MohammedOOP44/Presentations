from PIL import Image 

img = Image.open("ex.png")

resized = img.resize((1000,1000))
resized.save("output_resized.png")