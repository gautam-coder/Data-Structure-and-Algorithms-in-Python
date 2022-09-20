from linkedList import LinkedList

def sumlist(l1,l2):
    n1=l1.head
    n2=l2.head
    c=0
    l3=LinkedList()
    while n1 and n2:
        r=c
        if n1:
            r+=n1.value
            n1=n1.next
        if n2:
            r+=n2.value
            n2=n2.next
        l3.add(int(r%10))
        c=r/10
    return l3

l1=LinkedList()
l2=LinkedList()
l1.add(7)
l1.add(1)
l1.add(6)

l2.add(5)
l2.add(9)
l2.add(2)

print(l1)
print(l2)
print(sumlist(l1,l2))


        
