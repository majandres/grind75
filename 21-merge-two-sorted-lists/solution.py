from LinkedList import LinkedList, Node

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = Node()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 or list2

        head.display()
        return head
                




linked_list_a = LinkedList()
linked_list_a.append(1)
linked_list_a.append(2)
linked_list_a.append(4)

linked_list_b = LinkedList()
linked_list_b.append(1)
linked_list_b.append(3)
linked_list_b.append(4)


s = Solution()

s.mergeTwoLists(linked_list_a, linked_list_b)