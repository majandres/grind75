# https://leetcode.com/problems/merge-two-sorted-lists/

from LinkedList import LinkedList, Node

class Solution:
    """You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. 
    The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
    """
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