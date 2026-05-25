from PIL import Image 

img = Image.open("ex.png")

print("Format:",img.format)
print("Size:",img.size)
print("Mode:",img.mode)