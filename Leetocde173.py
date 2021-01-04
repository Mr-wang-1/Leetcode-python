# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        # O(h)内存，说明要用栈，不能使用队列等结构
        self.stack = []
        # 将左子节点依次入栈
        self._left_inorder(root)

    def _left_inorder(self, root):
        # 使用自己的栈模拟中序遍历
        # 模拟中序遍历“左根右”的“左”，依次将左子节点入栈
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # 两种情况
        # 1 当前节点无右子节点，则不用考虑
        # 2 当前节点有右子节点，则需对右子节点再进行中序遍历，即再调用_left_inorder()
        next_node = self.stack.pop()
        if next_node.right:
            self._left_inorder(next_node.right)
        return next_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
