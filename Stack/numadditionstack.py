s1 = []
s2 = []
s3 = []
car=0

def push(self, i):
    self.append(i)

def pop(self):
    self.pop(len(self)-1)

push(s1, 3)
push(s1, 7)
push(s1, 8)
push(s1, 4)
print(s1)
push(s2, 5)
push(s2, 9)
push(s2, 2)
print(s2)   

while s1!=[] or s2!=[]:
    if s1!=[] and s2!=[]:
        if s1.pop()+s2.pop()+car <10:
            push(s3,int(s1.pop())+int(s2.pop())+car)
            car=0
        else:
            push(s3,int(s1.pop)+int(s2.pop)+car-10)
            car=1

        
