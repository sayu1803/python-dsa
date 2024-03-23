
#Defining nodes
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

a=Node(1)
b=Node(2)
c=Node(3)
print (a)
print(a.data)#2748240852032
print(b.data)#2748240851984
print(c.data)#2748240852176

#connecting nodes

print(id(a))
print(id(b))
print(id(c))

a.next=b
b.next=c
#checking address values of the nodes
print(a.next)#0x000001CFD7997650
print(b.next)#0x000001CFD79976E0

#checking the values in decimal form
address_hex = '0x000001CFD7997650'
address_decimal = int(address_hex, 16)
print(address_decimal)
