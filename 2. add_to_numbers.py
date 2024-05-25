# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_str = ""
        second_str = ""

        # Collect values from the first list
        while l1:
            first_str += str(l1.val)
            l1 = l1.next

        # Collect values from the second list
        while l2:
            second_str += str(l2.val)
            l2 = l2.next
        
        # Reverse the collected strings and convert them to integers
        first_int = int(first_str[::-1])
        second_int = int(second_str[::-1])

        # Add the two integers
        result = first_int + second_int

        # Convert the result back to a string and reverse it to get the proper order
        result = str(result)[::-1]

        # Create the linked list from the result
        initial_node = ListNode(val=int(result[0]))
        current_node = initial_node
        for digit in result[1:]:
            new_node = ListNode(val=int(digit))
            current_node.next = new_node
            current_node = new_node

        return initial_node
