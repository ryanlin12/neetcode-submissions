from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #this uses the a-z approach
        #use hash where key is the array of numLetters and values are the words themselves
        
        anagramHash = defaultdict(list)
        # print(alphabetArray)
        for word in strs:
            alphabetArray = [0] * 26
            for letter in word:
                letterArrayIndex = ord(letter) - ord('a')
                alphabetArray[letterArrayIndex] += 1
            anagramHash[tuple(alphabetArray)].append(word)
        print(anagramHash.values())
        return list(anagramHash.values())