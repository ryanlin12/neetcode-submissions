class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numUnique = 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                numUnique += 1
                i += 1
        return numUnique