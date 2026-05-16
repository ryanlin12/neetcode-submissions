from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = defaultdict(int)
        returnArray = []
        # SEMI OPTIMAL
        # for index in range(0, len(nums)):
        #     numsDict[nums[index]] = index
        # for i in range(0, len(nums)):
        #     difference = target - nums[i]
        #     if difference in numsDict and i != numsDict[difference]:
        #         returnArray = [i, numsDict[difference]]
        #         return returnArray
                
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if (difference in numsDict):
                return [numsDict[difference], i]
            numsDict[nums[i]] = i