from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = defaultdict(list)
        tHash = defaultdict(list)
        for letter in s:
            sHash[letter].append(letter)
        for letter in t:
            tHash[letter].append(letter)
        print('sHash', sHash)
        print('tHash', tHash)
        return sHash == tHash
            