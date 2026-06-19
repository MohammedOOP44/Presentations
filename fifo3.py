class Node :
    def __init__(self,data):
        self.data = data 
        self.next = None

class Queue :
    def __init__(self):
        self.front = None 
        self.rear = None 

    def enqueue(self,item):
        new_node = Node(item)

        if self.front is None :
            self.rear = new_node
            self.front = new_node

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.rear is None :
            print("Queue underflow: nothing to remove")
            return None
        
        removed_value = self.front.data
        self.front = self.front.next
        
        if self.front is None :
            self.rear = None 

        return removed_value

    def display(self):
        if self.front is None :
            print("Queue is empty ")
            return 
        
        current = self.front
        elements = []
        while current is not None :
            elements.append(str(current))
            current = current.next
        print(f" --> ".join(elements))

Q = Queue()

Q.enqueue("task 1")
Q.enqueue("task 2")
Q.enqueue("task 3")

Q.diplay()

print(f"Removed: {Q.dequeue}")
Q.display()
