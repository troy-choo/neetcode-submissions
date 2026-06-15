class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: 
            return False

        count_s1  = {}
        for s in s1:
            count_s1[s] = 1 + count_s1.get(s, 0)

        for i in range(n2 - n1 + 1):
            sub_s2 = s2[i : i + n1]
            
            count_sub = {}
            for char in sub_s2:
                count_sub[char] = 1 + count_sub.get(char, 0)
            
            if count_s1 == count_sub:
                return True
        return False