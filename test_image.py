from PIL import Image 
img = Image.open("example.png")

print("format: ", img.format)
print("size: " , img.size)
print("mode: ", img.mode)
