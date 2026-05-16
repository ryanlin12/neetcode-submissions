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
            

        # for index, char in enumerate(s):
        #     leftPtr = index
        #     rightPtr = len(s) - 1 - leftPtr
        #     #print(isAlphaNumeric(char))
        #     print(leftPtr, s[leftPtr], ":", rightPtr, s[rightPtr])
        #     if not isAlphaNumeric(s[leftPtr]):
        #         #print("went left")
        #         leftPtr += 1
        #         continue
        #     if not isAlphaNumeric(s[rightPtr]):
        #         #print("went right")
        #         rightPtr -= 1
        #         continue
        #     if s[leftPtr] == s[rightPtr]:
                
                
        #         leftPtr += 1
        #         rightPtr -= 1
        #         if rightPtr <= leftPtr:
        #             return True
        #     else:
        #         return False
            #if s[leftPtr] != alphaNum
                #increment leftPtr
                #continue
            #if s[rightPtr] != alphaNum
                #decrement rightPtr
                #continue

            #if s[leftPtr] == s[rightPtr]:
                # increment & decrement
                #if rightPtr <= leftPtr
                    #return true
            #else
                #return false
def isAlphaNumeric(char: str) -> bool:
    return (ord('a') <= ord(char) <= ord ('z')
    or ord ('A') <= ord(char) <= ord('Z')
    or ord('0') <= ord(char) <= ord('9'))
            