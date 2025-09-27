class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = 0
        maxx = 0
        n = len(cardPoints)

        for i in range(k):
            total += cardPoints[i]

        maxx = total

        # begin sliding window

        for i in range(k):
            total -= cardPoints[k-i-1]
            total += cardPoints[n-i-1]
            maxx = max(maxx,total)

        return maxx