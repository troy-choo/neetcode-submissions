class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
        for c in s1:
            dic1[c] = 1 + dic1.get(c, 0)

        dic2 = {}
        l = 0

        for r in range(len(s2)):
            dic2[s2[r]] = 1 + dic2.get(s2[r], 0)

            if r - l + 1 > len(s1):
                dic2[s2[l]] -= 1

                if dic2[s2[l]] == 0:
                    del dic2[s2[l]]
                
                l += 1

            if dic1 == dic2:
                return True

        return False