class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def __iter__(self):
        t=self.head
        while t:
            yield t
            t=t.next
        
class stack:
    def __init__(self):
        self.LinkedList=LinkedList()
    def __str__(self):
        values=[str(i.val) for i in self.LinkedList]
        return "\n".join(values)
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
            
    def push(self,val):
        t=Node(val)
        t.next=self.LinkedList.head
        self.LinkedList.head=t
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        t=self.LinkedList.head.val
        self.LinkedList.head=self.LinkedList.head.next
        return t
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        t=self.LinkedList.head.val
        return t
    def delete(self):
        self.LinkedList.head=None
ss=stack()
ss.push(3)
ss.push(4)
ss.push(5)
print(ss)
print(ss.pop())
print(ss.peek())
ss.delete()
print(ss)
