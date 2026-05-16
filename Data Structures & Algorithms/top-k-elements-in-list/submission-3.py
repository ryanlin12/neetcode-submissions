from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap that has the count for each number that shows up
        #for each value that we get, we will put it into an array
            #Index of each array is the number of times we saw the number
        counthash = defaultdict(int)
        freqArray = [[] for i in range(0, len(nums) + 1)] #there could be multiple numbers at the same freq
        returnArray = []
        # returnArrayAddedCt = 0
        for num in nums:
            counthash[num] += 1
        for key, value in counthash.items():
            freqArray[value].append(key)
        for i in range(len(freqArray) - 1, 0, -1):  # go backwards
            # if (returnArrayAddedCt < k):
            for num in freqArray[i]:
                returnArray.append(num)
                if len(returnArray) == k:
                    return returnArray
        # return returnArray