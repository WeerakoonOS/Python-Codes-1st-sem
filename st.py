class Stack:
    def __init__ (self):
        self.items = []
    def __repr__ (self):
        return repr(self.items)
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def pop(self):
        return self.items.pop()
    def push(self, val):
        return self.items.append(val)
    def peek(self):
        return self.items[len(self.items)-1]

s=Stack()
s.push(67)
s.push(234)
s.push(455)
s.push(98)
s.push(104)
print(s)
s.pop()
print(s)
print(s.isEmpty())
print(s.pop())
print(s.peek())
print(s)
print(s.size())

