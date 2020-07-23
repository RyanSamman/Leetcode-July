# https://leetcode.com/problems/single-number-iii/


class Solution:
    def __init__(self):
        self.hash = {}

    def addNumber(self, i):
        if i in self.hash.keys():
            self.hash[i] += 1
        else:
            self.hash[i] = 1

    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums
        [self.addNumber(i) for i in nums]

        print(self.hash)
        return [key for key, val in self.hash.items() if val == 1]
