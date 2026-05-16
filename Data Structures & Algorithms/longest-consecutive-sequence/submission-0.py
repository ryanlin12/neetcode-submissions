from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        allSequences = defaultdict(set)
        for n in numSet:
            if n - 1 not in numSet:
                newSequence = set()
                newSequence.add(n)
                numToCheck = n + 1
                while numToCheck in numSet:
                    newSequence.add(numToCheck)
                    numToCheck = numToCheck + 1
                allSequences[len(newSequence)] = newSequence
        #print(allSequences)
        highestLength = 0
        for length, sequence in allSequences.items():
            if length > highestLength:
                highestLength = length
        print(highestLength)
        return highestLength
