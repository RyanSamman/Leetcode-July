binaryTreeArray = [3, 9, 20, None, None, 15, 7]


def parseTree(binaryTree):
    solution = []
    arrayLength = len(binaryTree)
    level = 0
    i = j = currentLevel = 0
    while i < len(binaryTree):
        currentLevel = 2 ** level
        j = 0
        levelArray = []
        while True:
            if i + currentLevel - j - 1 >= arrayLength:
                j += 1
                continue

            currentNode = binaryTree[i + currentLevel - j - 1]
            # print(currentNode)
            if currentNode is not None:
                levelArray.append(binaryTree[i + currentLevel - j - 1])

            j += 1

            if currentLevel - j - 1 < 0:
                break
        level += 1
        # print("new level")
        i += j
        solution.append(levelArray)

    solution.reverse()

    return solution


print(parseTree(binaryTreeArray))
