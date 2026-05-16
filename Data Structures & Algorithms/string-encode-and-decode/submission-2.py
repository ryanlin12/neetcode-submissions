class Solution:

    def encode(self, strs: List[str]) -> str:
        togetherString = ''
        for string in strs:
            togetherString += str(len(string)) + "#"
            for letter in string:
                togetherString += letter
        return togetherString
    def decode(self, s: str) -> List[str]:
        # strLength = int
        # returnList = []
        # print(s)
        # for index, char in enumerate(s):
        #     stringToAdd = ''
        #     if char == '#':
        #         if s[index-1].isdigit():
        #             strLength = int(s[index-1])
        #             for i in range(0, strLength):
        #                 charIndex = i + index + 1
        #                 stringToAdd += s[charIndex]
        #             returnList.append(stringToAdd)
        # return returnList
        returnList = []
        i = 0
        while i < len(s):
            j = i
            while (s[j] != '#'):
                j += 1
            
            length = int(s[i:j])
            returnList.append(s[j+1 : j+1+length])
            print(length)
            i = j+1+length
        return returnList

        
