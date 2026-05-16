from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #keys that identify what word belongs to what anagram
        #sort according to key
        #key will be an array with a counter of how frequent each letter arrives
        stringHash = defaultdict(list)
        for string in strs:
            letterCount = [0] * 26
            for char in string:
                letterIndex = ord(char) - ord('a')
                letterCount[letterIndex] += 1
            stringHash[tuple(letterCount)].append(string)
        return list(stringHash.values())