class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = {}, {}
        for keyS in s:
            dictS[keyS] = 1 + dictS.get(keyS, 0)
        for keyT in t:
            dictT[keyT] = 1 + dictT.get(keyT, 0)
        if dictS == dictT:
            return True
        return False