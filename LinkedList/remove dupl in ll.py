from linkedList import LinkedList

def removeDup(ll):
    if ll.head is None:
        return
    else:
        temp=ll.head
        vv=set([temp.value])
        while temp.next:
            if temp.next.value in vv:
                temp.next=temp.next.next
            else:
                vv.add(temp.next.value)
                temp=temp.next
        return ll
def removedup1(ll):
    if ll.head is None:
        return
    else:
        temp=ll.head
        while temp.next:
            a=temp.value
            t=temp
            while t.next:
                if t.next.value==a:
                    t.next=t.next.next
                else:
                    t=t.next
            temp=temp.next

a=LinkedList()
a.generate(10,5,10)
print(a)
removedup1(a)
print(a)
