# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            current = head
            holder = []
            for i in range(k):
                if current.next is None:
                    return None, None
                holder.append(current.next)
                current = current.next
            holder[0].next = holder[-1].next
            for i in range(k-1):
                holder[i+1].next = holder[i]
            return holder[0], holder[-1]
        
        new_head = ListNode()
        new_head.next = head
        
        a, b = reverse(new_head, k)
        new_head.next = b
        current = a
        
        while True:
            a, b = reverse(current, k)
            if a is None:
                return new_head.next
            else:
                current.next = b
                current = a

