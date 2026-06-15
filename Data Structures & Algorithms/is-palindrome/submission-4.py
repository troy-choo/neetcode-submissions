class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        lowerS = s.lower()
        reversedS = "".join(s[::-1])
        if lowerS == reversedS:
            return True
        return False