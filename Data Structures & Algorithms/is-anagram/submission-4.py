from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # setS = set()
        # setT = set()
        # for S in s:
        #     setS.add(S)
        # for T in t:
        #     setT.add(T)
        # return setS == setT and len(s) == len(t)
        sMap = defaultdict(list)
        tMap = defaultdict(list)
        for S in s:
            sMap[S].append(S)
        for T in t:
            tMap[T].append(T)
        print(sMap, tMap)
        return sMap == tMap

