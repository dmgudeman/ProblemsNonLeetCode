# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.



class Solution:
    def middleNode(self, head):
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow