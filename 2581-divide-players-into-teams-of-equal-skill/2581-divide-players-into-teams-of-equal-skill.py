class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()

        l,r = 0,len(skill)-1
        prod = 0
        summ = -1
        while l <= r:
            
            if (skill[l]+skill[r]) == summ or summ == -1:
                summ = skill[l] + skill[r]

            else:
                return -1

            prod += (skill[l] * skill[r])
            l += 1
            r -= 1


        return prod
