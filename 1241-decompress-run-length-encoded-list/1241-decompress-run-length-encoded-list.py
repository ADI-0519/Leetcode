class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            data = nums[i+1]
            for j in range(0,freq):
                lst.append(data)

        return lst