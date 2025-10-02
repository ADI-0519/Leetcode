class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float("inf")] * (n)
        dist[src] = 0

        for i in range(k+1):

            temp = dist.copy()

            for u,v, weight in flights:
                if dist[u] == float("inf"):
                    continue

                if dist[u] + weight < temp[v]:
                    temp[v] = dist[u] + weight

            dist = temp

        return -1 if dist[dst] == float("inf") else dist[dst]
                