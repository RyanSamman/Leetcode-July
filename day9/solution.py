# Warning - I failed this day, this code doesn't work properly
binaryTreeArray = [3, 9, 20, None, None, 15, 7]


class Solution:
    def widthOfBinaryTree(self, tree):
        parsed = self.levelOrderBottom(tree)
        i = 0
        for level in parsed:
            hasDistance = self.getSize(level)
            if hasDistance:
                print("Distance is", hasDistance)
                return hasDistance

    @staticmethod
    def getSize(level: list):
        length = len(level)
        print(level)
        distance = 0
        left = 0
        right = len(level) - 1
        while level[left] is None:
            left += 1
            if left == length - 1:
                return 0

        while level[right] is None:
            right -= 1

        if right == left:
            return 0

        while right >= left:
            print(level[left])
            left += 1
            distance += 1

        print("Distance is", distance)
        if distance <= 0:
            return 0
        return distance

    @staticmethod
    def levelOrderBottom(root):
        solution = []

        def addArray(value, depth):
            # print(value, depth)
            try:
                solution[depth].append(value)
            except IndexError:
                # print("Index Error", value, depth)
                solution.append([value])

        def walkTree(tree, depth=0):
            try:
                addArray(tree.val, depth)
            except AttributeError:
                addArray(None, depth)

            depth += 1
            
            walkTree(tree.left, depth)
            walkTree(tree.right, depth)

        walkTree(root)
        solution.reverse()
        return solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    root = TreeNode(1)
    # [1, 1, 1, 1, None, None, 1, 1, None, None, 1]
    root.left = TreeNode(3)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)

    root.right = TreeNode(2)

    root.right.right = TreeNode(9)

    x = Solution()
    x.widthOfBinaryTree(root)
    # x.getSize([None, None, 5, None, 3, None, 9, None])

