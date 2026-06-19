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

        if self.rear is None :
            self.front = new_node 
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node 
        print(f"Enqueue: {item}")

    def dequeue(self):
        if self.front is None :
            print("Queue underflow: nothing to remove")
            return None 
        
        removed_value = self.front.data

        self.front = self.front.next

        if self.front is None:
            self.rear = None 

        return removed_value 


    def display(self):
        if self.front is None :
            print("Queue is empty")
            return 
        
        current = self.front 
        elements = []
        while current is not None :
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))


myQueue = Queue()

myQueue.enqueue("Task 1")
myQueue.enqueue("Task 2")
myQueue.enqueue("Task 3")
myQueue.display()

print(f"removed: {myQueue.dequeue()}")
myQueue.display()


