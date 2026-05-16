class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        print(numSet)
        for i, num in enumerate(nums):
            if num in numSet:
                return True
            numSet.add(num)
        return False

