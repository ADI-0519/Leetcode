class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = sum(cardPoints[:k])
        maxx = total
        n = len(cardPoints)

        # begin sliding window

        for i in range(k):
            total -= cardPoints[k-i-1]
            total += cardPoints[n-i-1]
            maxx = max(maxx,total)

        return maxx