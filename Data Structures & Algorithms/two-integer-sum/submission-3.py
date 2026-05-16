from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = defaultdict()
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in numDict:
                return [numDict[difference], i]
            numDict[nums[i]] = i
