class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #remove duplicates
        arrayOfSeqs = []
        firstSet = set()
        highestSequenceSize = 0
        #we create a new set for eqch sequence
            #if num + 1 in set
                #we append it to the set
            #if num + 1 NOT in set
                #create a new set
        for num in numSet:
            if num - 1 not in numSet:
                newSequence = set()
                newSequence.add(num)
                numToCheck = num + 1
                while numToCheck in numSet:
                    newSequence.add(numToCheck)
                    numToCheck = numToCheck + 1
                if (len(newSequence) > highestSequenceSize):
                    highestSequenceSize = len(newSequence)

        return highestSequenceSize
