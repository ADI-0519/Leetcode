class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = 0
        maxx = 0
        n = len(cardPoints)

        for i in range(k):
            total += cardPoints[i]

        maxx = total

        # begin sliding window

        for i in range(1,k+1):
            total -= cardPoints[k-i]
            total += cardPoints[n-i]
            maxx = max(maxx,total)

        return maxx