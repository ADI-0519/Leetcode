class Solution(object):
    def twoSum(self,nums, target):
        hashmap = {}
        for i,element in enumerate(nums):
            if (target-element) not in hashmap:
                hashmap[element] = i
            else:
                return hashmap.get(target-element),i

        
        