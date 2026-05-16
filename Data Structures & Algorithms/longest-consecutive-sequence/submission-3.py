from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        allSequences = defaultdict(set)
        highLength = 0
        for n in numSet:
            if n - 1 not in numSet:
                newSequence = set()
                newSequence.add(n)
                numToCheck = n + 1
                while numToCheck in numSet:
                    newSequence.add(numToCheck)
                    numToCheck = numToCheck + 1
                if len(newSequence) > highLength:
                    highLength = len(newSequence)
        return highLength
