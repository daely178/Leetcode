# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightside = []
        def helper(node, depth):
            if node:
                if depth == len(rightside):
                    rightside.append(node.val)
                helper(node.right, depth+1)
                helper(node.left, depth+1)
        helper(root, 0)
        return rightside


    def rightSideView2(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        rightside = []

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                # if it's the rightmost element
                if i == level_length - 1:
                    rightside.append(node.val)

                # add child nodes in the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightside
