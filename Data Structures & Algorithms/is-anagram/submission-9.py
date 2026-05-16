from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = defaultdict(int)
        tHash = defaultdict(int)

        for letter in s:
            sHash[letter] = sHash[letter] + 1
        for letter in t:
            tHash[letter] = tHash[letter] + 1
        return sHash == tHash
