from collections import deque, defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(list)

        for x, y, z in times:
            adj_list[x].append((y,z))

        # Stores node -> (other node, weight)

        min_times = {}
        heap = [(0,k)]
        
        while heap:
            dist, node = heapq.heappop(heap)

            if node in min_times:
                continue

            min_times[node] = dist
            for nei,weight in adj_list.get(node,[]):
                if nei not in min_times:
                    heapq.heappush(heap, (dist+weight,nei))

        if len(min_times) == n:
            return max(min_times.values())

        else:
            return -1