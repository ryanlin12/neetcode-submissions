class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode: "4#neet4#code4#love3#you"
        allString = ''
        for string in strs:
            stringLength = len(string)
            allString = allString + str(stringLength) + '#' + string
        return allString
    def decode(self, s: str) -> List[str]:
        #print(s[0])
        returnArray = []
        i = 0
        j = 0
        strLength = 0
        while i < len(s):
            j = i
            while (s[j] != '#'):
                j += 1
            strLength = int(s[i:j])
            returnArray.append(s[j + 1 : j + 1 + strLength])  #"4hello"
            i = j + 1 + strLength
        print(returnArray)
        return returnArray



