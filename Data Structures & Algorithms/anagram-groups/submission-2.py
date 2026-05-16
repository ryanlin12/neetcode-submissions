from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringHash = defaultdict(list)
        #anagramHash = defaultdict(str) 
        letterCount = [] #array to count the # of each letter in a string
        for string in strs:
            #anagramHash.clear()
            letterCount = [0] * 26 # 26 0's for a-z
            for s in string:
                #below is the hash map of a string
                #two anagrams will have the same hashmap
                #anagramHash[s] = anagramHash[s] + s 
                letterCount[ord(s) - ord("a")] += 1

            #allows you to put a hashmap as a key for another hashmap
            stringHash[tuple(letterCount)].append(string) 
        return list(stringHash.values())