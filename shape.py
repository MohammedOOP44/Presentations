import turtle

points = [] 

print("--- Enter the coordenates ---")

for i in range(10):
    print(f"Enter the data of point {i+1}:")
    
    user_x = input("X: ") 
    x = int(user_x) 
    
    user_y = input("Y: ")
    y = int(user_y)
    points.append([x,y])

t = turtle.Turtle()
t.speed(5) 

# التحدي 3: "القفزة الأولى"
# القائمة 'points' ممتلئة الآن. العنصر الأول هو points[0]
# السلحفاة في المركز (0,0). نريدها أن تذهب للنقطة الأولى دون رسم خط.

t.penup()
# نستخرج النقطة الأولى من القائمة
start_point = points[0]  
# start_point الآن عبارة عن [x, y] الخاصة بأول مدخل

# نذهب إليها
t.goto(start_point[0], start_point[1]) 

t.pendown() # الآن ننزل القلم للبدء الفعلي


for point in points:
    
    t.goto(point[0],point[1])

turtle.done()