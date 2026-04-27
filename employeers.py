import tkinter as tk
class Item :
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (Qty: {self.quantity})"
    
class ItemManagementSystem:
    def __init__(self):
        self.items = []

    def add_item(self,name,quantity):
        item = Item(name,quantity)
        self.items.append(item)

    def remove_item(self,name):
        self.items = [item for item in self.items if item.name != name]

    def get_item(self):
        return self.items
    
class ItemApp:
    def __init__(self,window):
        self.window = window
        self.system = ItemManagementSystem()
        self.window.title("Item App")

        tk.Label(window,text="item Name").pack()
        self.name_entry = tk.Entry(window)
        self.name_entry.pack()

        tk.Label(window,text="Quantity").pack()
        self.Quantity_entry = tk.Entry(window)
        self.Quantity_entry.pack()

        tk.Button(window,text='add item',command=self.add_item).pack()
        tk.Button(window,text='remove item',command=self.remove_item).pack() 

        self.listbox = tk.Listbox(window,width=55)
        self.listbox.pack()

    def add_item(self):
        name = self.name_entry.get()
        Qty = int(self.Quantity_entry.get())
        self.system.add_item(name,Qty)
        self.update_listbox()

    def remove_item(self):
        selection = self.listbox.curselection()
        if selection :
            item_text = self.listbox.get(selection[0])
            item_name = item_text.split(" (")[0]
            self.system.remove_item(item_name)
            self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0,tk.END)
        for item in self.system.get_item():
            self.listbox.insert(tk.END,str(item))


window = tk.Tk()
app = ItemApp(window)
window.mainloop()
        