from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hash map to get the number of times each number appears in array
        #array of n + 1 elements(ex. 0-6) where each index is a list
            #that indicates number of times a number showed up
            

        numHash = defaultdict(int)
        #adding plus 1 so that 7th index = number showed up 7 times
        freqArray = [[] for i in range(0, len(nums) + 1)]
        returnArray = []

        for num in nums:
            numHash[num] += 1
        for num, count in numHash.items():
            freqArray[count].append(num)
        print(freqArray)
        #start, end, direction
        for i in range(len(freqArray) - 1, -1, -1):
            print(i)
            for num in freqArray[i]:
                returnArray.append(num)
            if len(returnArray) == k:
                return returnArray
        