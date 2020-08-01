class Solution:
    def levelOrderBottom(self, root):
        solution = []

        def addArray(value, depth):
            # print(value, depth)

            try:
                solution[depth].append(value)
            except IndexError:
                # print("Index Error", value, depth)
                solution.append([value])

        def walkTree(tree, depth=0):
            if tree is None:
                return

            addArray(tree.val, depth)
            depth += 1
            if tree.left is not None:
                walkTree(tree.left, depth)
            if tree.right is not None:
                walkTree(tree.right, depth)

        walkTree(root)
        solution.reverse()
        return solution