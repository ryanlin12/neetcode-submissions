class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1 - l
        while l < r:
            if isAlphaNumeric(s[l]) and isAlphaNumeric(s[r]):
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
            else:
                if not isAlphaNumeric(s[l]):
                    l += 1
                if not isAlphaNumeric(s[r]):
                    r -= 1
        return True

def isAlphaNumeric(char: str) -> bool:
    return (ord('a') <= ord(char) <= ord ('z')
    or ord ('A') <= ord(char) <= ord('Z')
    or ord('0') <= ord(char) <= ord('9'))
            