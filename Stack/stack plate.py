class plate:
    def __init__(self,cap):
        self.cap=cap
        self.stacks=[]

    def push(self,item):
        if len(self.stacks)>0 and len(self.stacks[-1])<self.cap:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1])==0:
            self.stacks.pop()
        if len(self.stacks)<=0:
            return None
        else:
            self.stacks[-1].pop()
            print(self.stacks)
    def pop_at(self,no):
        if len(self.stacks[no])>0:
            return self.stacks[no].pop()
        else:
            return None

pp=plate(2)
pp.push(2)
pp.push(3)
pp.push(4)
pp.push(5)
pp.push(6)
pp.push(7)

print(pp.pop())
print(pp.pop())
print(pp.pop())
print(pp.pop_at(1))
