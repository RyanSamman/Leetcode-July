class Solution:
    @staticmethod
    def subsets(nums):
        numberOfSubsets = 2 ** len(nums)

        def generateSubset(i):
            binary = int(str(bin(i))[2:])
            subset, index = [], 0
            while True:
                if binary % 10 != 0:
                    subset.append(nums[index])
                index += 1
                binary //= 10
                if binary == 0:
                    break
            return subset

        return [generateSubset(i) for i in range(0, numberOfSubsets)]


if __name__ == '__main__':
    x = Solution()
    x.subsets([1, 2])


# Each set has n
# (1, 2)
# {}     00
# {1}    01
# {2}    10
# {1, 2} 11
