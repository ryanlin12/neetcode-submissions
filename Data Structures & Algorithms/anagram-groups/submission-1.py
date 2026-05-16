from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringHash = defaultdict(list)
        anagramHash = defaultdict(str)
        #hasmap keys will be the sorted string
        #we insert the strings as values into the corresponding key 
        for string in strs:
            anagramHash.clear()
            for s in string:
                anagramHash[s] = anagramHash[s] + s #sorted string
            print(anagramHash.items())
            # sortedString = ''.join(sorted(string))
            # anagramList.append(anagramHash)
            stringHash[frozenset(anagramHash.items())].append(string) #allows you to put a hashmap as a key for another hashmap
        return list(stringHash.values())