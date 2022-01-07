# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        # Resevoir Sampling
        # https://florian.github.io/reservoir-sampling/
        
        resevoir = self.head.val
        
        next = self.head.next
        
        i = 2
        while next:
            if random.random() < 1/i:
                resevoir = next.val
            
            i += 1
            next = next.next
            
        return resevoir
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()