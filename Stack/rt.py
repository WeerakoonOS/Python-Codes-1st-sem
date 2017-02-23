class Stack:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return repr(self.items)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self,val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
q=Stack()
q.push('a')
q.push('b')
q.push('c')
print(q)
q.push('f')
print(q)
q.pop()
print(q)
q.pop()
q.pop()
print(q)
