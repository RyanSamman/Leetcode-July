#https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
                continue
            hash[i] += 1
        
        arr = []
        keys = hash.keys()

        for i in keys:
            arr.append(i)
            
        arr.sort(key=lambda x: hash[x])
        
        return arr[-k:]