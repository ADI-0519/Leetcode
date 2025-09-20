from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        q = deque()

        for i in range(k):

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)


        arr.append(nums[q[0]])


        for i in range(k,len(nums)):

            # remove from the left

            while q and q[0] <= i-k:
                q.popleft()

            
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)
            arr.append(nums[q[0]])

        return arr