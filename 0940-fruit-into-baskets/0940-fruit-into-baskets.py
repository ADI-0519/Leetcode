class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        p1 = 0
        longest = 0
        hashmap = {}
        for p2 in range(len(fruits)):
            hashmap[fruits[p2]] = hashmap.get(fruits[p2],0) + 1
            
            while len(hashmap)>2:
                hashmap[fruits[p1]] = hashmap.get(fruits[p1],0) - 1 
                if hashmap[fruits[p1]] <= 0:
                    del hashmap[fruits[p1]]

                p1 += 1
            

            length = (p2-p1) + 1

            if length >= longest:
                longest = length

        return longest
            
