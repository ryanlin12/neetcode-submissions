from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyArray = [[] for i in range(len(nums) + 1)] #list of lists because multiple numbers could have the same freq
        frequencyHash = defaultdict(int) #int for freq of each number
        returnArray = []
        #hashMap to keep track of how frequent each number comes in
        #print(frequencyArray)
        for num in nums:
            frequencyHash[num] += 1
        #print(frequencyHash)
        for num, freq in frequencyHash.items():
            #print(num, freq)
            frequencyArray[freq].append(num)
        print(frequencyArray)
        numsTaken = 0
        for i in range(len(frequencyArray)-1, -1, -1):
            #print(i)
            #print(frequencyArray[i])
            for num in frequencyArray[i]:
                returnArray.append(num)
            if len(returnArray) == k:
                return returnArray

        

        #array of size nums where the index is the number of times the number is in the array
        #we insert into that array and return top k most frequent