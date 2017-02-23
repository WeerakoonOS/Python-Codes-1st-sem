class Stack:
    def _init_ (self):
        self.items = []
    def _repr_(self):
        return repr(self.items)
    def push (self, element):
        return self.items.append(element)
    def pop(self):
        return self.items.pop(len(self.items)-1)
    def peek(self):
        return self.items(len(self.items)-1)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return (self.items==[])

class Queue:
    def _init_ (self):
        self.items=[]
    def _repr_(self):
        return repr(self.items)
    def enqueue(self, element):
        return self.items.append(element)
    def dequeue():
        return self.items.pop(0)
    def top(self):
        return self.items[0]
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)

q=Queue
enqueue(q,12)
q.isEmpty()
    
