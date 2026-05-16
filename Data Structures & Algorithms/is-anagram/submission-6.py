from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(list)
        tDict = defaultdict(list)
        for S in s:
            sDict[S].append(S)
        for T in t:
            tDict[T].append(T)
        return sDict == tDict
        