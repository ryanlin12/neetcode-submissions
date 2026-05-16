from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(list)
        tMap = defaultdict(list)
        for S in s:
            sMap[S].append(S)
        for T in t:
            tMap[T].append(T)
        print(sMap, tMap)
        return sMap == tMap

