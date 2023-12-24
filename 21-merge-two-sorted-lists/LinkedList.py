# Benefits of using an array, we can access any indice in constant time. O(1)
# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node()


    def append(self, val):
        node = Node(val=val)
        current = self.head

        # move through the nodes, until the last one is reached
        while current.next != None:
            current = current.next

        # we're at the last node, set 'next' to the new node created just above
        current.next = node


    def length(self):
        current = self.head
        count = 0

        while current.next != None:
            current = current.next
            count += 1

        return count


    def display(self):
        vals = []
        current = self.head

        while current.next != None:
            current = current.next
            vals.append(current.val)
        print(vals)


    def get(self, index):
        if index >= self.length() or index < 0:
            print(f"ERROR: Index '{index}' is out of range")
            return None
        
        current = self.head
        count = 0

        while True:
            current = current.next
            if index == count:
                return current.val
            count += 1


    def remove(self, index):
        if index >= self.length() or index < 0:
            print(f"ERROR: Index '{index}' is out of range")
            return None
        
        current = self.head
        count = 0

        while True:
            last = current  # keep a ref to the previous node
            current = current.next

            if index == count:
                # skip the currentrent node and point to the following node
                current = current.next
                last.next = current 
                return True
            
            count += 1

