class Solution:
    def reorderList(self, head: ListNode) -> None:       
        if not head or not head.next:
            return head
        # 用快慢指针把链表一分为二，前半部分长度 >= 后半部分长度
        # first 为前半部分的头部，second 为后半部分的头部
        first = low = fast = head
        while fast.next and fast.next.next:
            fast, low = fast.next.next, low.next
        second, node, low.next, second.next = low.next, low.next.next, None, None
        # 后半部分逆序
        while node:
            node.next, second, node = second, node, node.next
        # 前后部分交替链接
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next