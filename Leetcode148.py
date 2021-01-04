# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        from queue import PriorityQueue
        ptr = head
        p_queue = PriorityQueue()
        while ptr != None:
            p_queue.put(ptr.val)
            ptr = ptr.next
            
        ptr = head
        while not p_queue.empty():
            ptr.val = p_queue.get()
            ptr = ptr.next
        return head
