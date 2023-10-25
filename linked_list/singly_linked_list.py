# construction of node 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


# a linked list where head and tail point to one node with length 1
# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1 


# new_list = LinkedList(10)
# print(new_list.head.value)
# print(new_list.tail.value)
# print(new_list.length)


# a linked list empty
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

new_linkedlist = LinkedList()
new_linkedlist.append(10)
new_linkedlist.append(20)
new_linkedlist.append(30)

print(new_linkedlist.head.value)
print(new_linkedlist.tail.value)
print(new_linkedlist.length)

            