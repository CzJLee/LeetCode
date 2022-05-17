# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq
# Solution using heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def get_next(llist):
            while llist is not None:
                next_val = llist.next
                yield llist
                llist = next_val

        
        iterable_llists = [get_next(llist) for llist in lists]
        heap = heapq.merge(*iterable_llists, key = lambda x: x.val)
        
        head = ListNode()
        current = head
        for node in heap:
            current.next = node
            current = current.next
            
        return head.next