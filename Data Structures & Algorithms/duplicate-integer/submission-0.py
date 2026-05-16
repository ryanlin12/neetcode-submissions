from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = defaultdict(list)
        for n in nums:
            numHash[n].append(n)
        print(numHash.items())
        for key, value in numHash.items():
            if len(value) > 1:
                return True
        return False