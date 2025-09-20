class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()

        l,r = 1,len(skill)-2
        prod = skill[0] * skill[len(skill)-1]
        total_skill = skill[0] + skill[len(skill)-1]

        while l <= r:
            
            if (skill[l]+skill[r]) == total_skill:
                prod += (skill[l] * skill[r])
                l += 1
                r -= 1

            else:
                return -1



        return prod
