import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = nums[:k]
        heapq.heapify(heap)
        for item in nums[k:]:
            if len(heap) >= k:
                heapq.heappushpop(heap,item)
            else:
                heapq.heappush(heap,item)

        return heap[0]