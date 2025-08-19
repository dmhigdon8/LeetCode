from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next  # Store the next node
            curr.next = prev      # Reverse the current node's pointer
            prev = curr           # Move prev to the current node
            curr = next_node      # Move curr to the next node in the original list
        
        return prev
    
ll = Solution()
print(ll.reverseList(head=[1, 2, 3, 4, 5]))  # Example usage, should return the reversed list
