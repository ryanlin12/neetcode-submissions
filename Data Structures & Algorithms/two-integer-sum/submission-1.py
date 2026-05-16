from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = defaultdict(int)
        returnArray = []
        for index in range(0, len(nums)):
            numsDict[nums[index]] = index
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in numsDict and i != numsDict[difference]:
                returnArray = [i, numsDict[difference]]
                return returnArray
                