from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
my_queue = Queue()
my_queue.enqueue("Alice")
my_queue.enqueue("Bob")
print(my_queue.peek())
print(my_queue.dequeue())
print(my_queue.size())