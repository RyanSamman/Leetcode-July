# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levelArr = []
        def addArr(value, level):
            try:
                levelArr[level].append(value)
            except (IndexError):
                levelArr.append([value])
        def walkTree(node, level=0):
            if node is None:
                return
            addArr(node.val, level)
            if node.left is not None:
                walkTree(node.left, level + 1)
            if node.right is not None:
                walkTree(node.right, level + 1)
            
            
        walkTree(root)
        [levelArr[i].reverse() for i in range(len(levelArr)) if i % 2 != 0]
        return levelArr