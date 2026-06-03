"""     ***(Typical Exam Wordings)****
"Implement a Queue data structure using a Singly Linked List."

"Write a class/struct to support enqueue() and dequeue() operations using a linked list representation."

"Design a FIFO (First-In, First-Out) queue without using arrays or built-in list methods."""

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None # Pointer to the next node in line (starts as empty)

# A queue needs to keep track of two crucial positions: the front (where people leave/dequeue) and
# the rear (where people join/enqueue). When you first create the queue, it's completely empty.

class Queue :
    def __init__(self):
        self.front = None # Tracks the first element
        self.rear = None # Tracks the last element

    def __str__(self):
        if self.front is None :
            return "Empty Queue"
        
        elements = []
        current = self.front # Start at the beginning

        while current is not None :
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements)

    def enqueue(self,item):
        new_node = Node(item)

        if self.rear is None :
            self.front = new_node 
            self.rear = new_node 
            return 
        
        self.rear.next = new_node 
        self.rear = new_node

# 2. Removing an item from the FRONT of the line
    def dequeue(self): 
        if self.front is None :
            print("Queue underflow!")
            return None 
        
        removed_data = self.front.data
        self.front = self.front.next

        if self.front is None :
            self.rear = None 
            
        return removed_data 
    
q = Queue()

print("--- Enqueuing Items ---")
q.enqueue("AAA")
q.enqueue("BBB")

print(q)

print("\n--- Dequeuing Items ---")

print(q.dequeue(),"left the line")
print(q.dequeue(),"left the line")

print("\n--- Testing Edge Case (Underflow) ---")
print(q.dequeue())
