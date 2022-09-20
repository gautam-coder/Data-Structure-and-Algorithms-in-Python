class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
    def __str__(self):
        string=str(self.value)
        if self.next:
            string+=','+str(self.next)
        return string

class stack():
    def __init__(self):
        self.top=None
        self.mi=None
    def __str__(self):
        #j=[str(i.value) for i in self.mi]
        return str(self.mi)
    def min(self):
        if not self.mi:
            return None
        return self.mi.value
    def push(self,items):
        if self.mi and self.mi.value<items:
            self.mi=Node(value=self.mi.value,next=self.mi)
        else:
            self.mi=Node(value=items,next=self.mi)
        self.top=Node(value=items,next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.mi=self.mi.next
        print(self.mi.value,"::::")
        item=self.top.value
        self.top=self.top.next
        return item
cs=stack()
cs.push(5)
cs.push(6)
cs.push(3)
cs.push(7)
print(cs)
cs.pop()
print(cs.min())
cs.pop()
print(cs.min())

