class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #진짜 유명한 알고리즘임.. 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT