from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringHash = defaultdict(list)
        for string in strs:
            letterCount = [0] * 26 # array of twentysix 0's for a-z
            for s in string: 
            #ascii number of letter - ascii of "a" = index of that letter in array
                #ex: find b
                #a: 80, b: 81
                #81 - 80 = index 1
                letterCount[ord(s) - ord("a")] += 1
            #allows you to put a hashmap as a key for another hashmap
            stringHash[tuple(letterCount)].append(string) 
        return list(stringHash.values())