from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = defaultdict(int) #for fast lookup
        for i, num in enumerate(nums):
            difference = target - num
            if difference in numsHash.keys():
                return [numsHash[difference], i]
            numsHash[num] = i