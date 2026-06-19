class Node :
    def __init__(self,data):
        self.data = data  # Stores the actual value (like 'A', 'B', 'C')
        self.next = None  # EXTRA MEMORY: Holds the pointer to the next node

class Queue :
    def __init__(self):
        self.front = None  # Tracks the exit (where we dequeue)
        self.rear = None   # Tracks the entrance (where we enqueue)

    def enqueue(self,item):
        new_node = Node(item) # Create the new dynamic element

        # If queue is empty, this new node is both front and rear
        if self.rear is None :
            self.front = new_node 
            self.rear = new_node 
            return 
        
        # Otherwise, link the old rear to the new node, then move rear forward
        self.rear.next = new_node 
        self.rear = new_node 
        print(f"Enqueue: {item}")


    def dequeue(self):
        # Check underflow (Is the queue empty?)
        if self.front is None :
            print("Queue underflow: nothing to remove")
            return None 
        
        # Save the data we want to return
        removed_value = self.front.data

        # NO SHIFTING: Just point 'front' to the next node in line
        self.front = self.front.next

        # If the queue is now empty, reset the rear pointer too
        if self.front is None :
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
        print(f"-->".join(elements))


# Test Drive
my_queue = Queue()

my_queue.enqueue("Task 1")
my_queue.enqueue("Task 2")
my_queue.enqueue("Task 3")
my_queue.display()  # Output: Task 1 -> Task 2 -> Task 3

print(f"Removed: {my_queue.dequeue()}")
my_queue.display()  # Output: Task 2 -> Task 3 (No shifting occurred in memory!)



