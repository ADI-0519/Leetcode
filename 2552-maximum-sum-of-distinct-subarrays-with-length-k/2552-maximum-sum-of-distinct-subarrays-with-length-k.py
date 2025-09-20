class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        summ = 0
        largest = 0
        hashmap = {}
        
        for i in range(k):
            summ += nums[i]
            hashmap[(nums[i])] = hashmap.get(nums[i],0) + 1

        if len(hashmap) >= k and summ > largest:
            largest = summ

        for j in range(k,len(nums)):
            summ -= nums[j-k]

            hashmap[(nums[j-k])] = hashmap.get(nums[j-k],0) - 1

            if hashmap[nums[j-k]] <= 0:
                del hashmap[nums[j-k]] 
            
            summ += nums[j]
            
            hashmap[(nums[j])] = hashmap.get(nums[j],0) + 1

            if len(hashmap) >= k and summ > largest:
                largest = summ

        return largest