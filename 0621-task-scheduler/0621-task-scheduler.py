import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        c = Counter(tasks)
        heap = [-val for val in c.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()
        
        while heap or q:
            time += 1
            
            if heap:
                item = heapq.heappop(heap)
                item += 1
                if item != 0:
                    q.append((item,time+n))

            # check can we add any tasks from the queue

            if q and q[0][1] == time:
                item = q.popleft()
                heapq.heappush(heap,item[0])

        return time
                

