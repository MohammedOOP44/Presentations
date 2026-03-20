lis = []
class User :
    def __init__(self,product,type,model,price):
        self.product = product
        self.type = type 
        self.model = model
        self.price = price
    def user_display(self):
        print(f"product: {self.product}")
        print(f"Type: {self.type}")
        print(f"model: {self.model}")
        print(f"price: {self.price}")
def add_custmor():
    product = input("Enter the product: ")
    type = input("Enter the type: ")
    model = input("Enter the model: ")
    price = input("Enter the price: ")

    product = User(product,type,model,price)
    return product
    

while True:
    print("________________________")
    print("choose an action")
    print("1.buy")
    print("2.cart display")
    print("3.Exit")
    choose = int(input("Enter your choice: "))
    print("_____________________________________________")
    if choose == 1:
        product100 = add_custmor()
        product100.user_display()
        lis.append(product100)
        


    elif choose == 2:
        for x in lis:
           x.user_display()
    else:
        print("Exiting...")
        break
        


        
