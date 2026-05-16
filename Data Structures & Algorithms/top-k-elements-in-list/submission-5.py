from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap to store number & how frequent they appear
        #bucket sort into arrays to sort how frequent each element shows up
            #each bucket is a frequency (or num times number shows up)
        numHash = defaultdict(int)
        returnArray = []
        frequencyArray = [[] for i in range(0, len(nums) + 1)]
        print(range(0, 10))
        #fill in hashmap
        for num in nums:
            numHash[num] += 1
        #now use hashmap to bucket sort into array
        for number, count in numHash.items():
            frequencyArray[count].append(number)
        #print(frequencyArray)
        #now return the last two eleemnts in frequencyArray
        print("length of freqArray", len(frequencyArray))
        for n in range(len(frequencyArray) - 1, -1, -1):
            for num in frequencyArray[n]:
                returnArray.append(num)
                if (len(returnArray) == k):
                    return returnArray
