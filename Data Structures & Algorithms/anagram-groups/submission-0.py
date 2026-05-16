from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringHash = defaultdict(list)
        #hasmap keys will be the sorted string
        #we insert the strings as values into the corresponding key 
        for string in strs:
            sortedString = ''.join(sorted(string))
            stringHash[sortedString].append(string)
        return list(stringHash.values())