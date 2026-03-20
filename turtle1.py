import random
shapes = ["square","circle","triangle","rectangle","oval"]
shapes.insert(2,"parallelogram")
print(shapes)
random_shape = random.choice(shapes)
print(random_shape)
5