from collections import defaultdict
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnArray = []
        #Prefix products
        lenOfNums = len(nums)
        #print(lenOfNums)
        prefixProducts = [0] * lenOfNums
        prefixProducts[0] = nums[0]
        suffixProducts = [0] * lenOfNums
        suffixProducts[lenOfNums - 1] = nums[lenOfNums - 1]
        #print(suffixProducts[lenOfNums-1])
        for i in range(1, lenOfNums):
            prefixProducts[i] = prefixProducts[i-1] * nums[i]
        #Suffix products
        for i in range(lenOfNums-2, -1, -1):
            #print(i, nums[i])
            suffixProducts[i] = suffixProducts[i+1] * nums[i]
        print(prefixProducts)
        print(suffixProducts)
        for i in range (0, lenOfNums):
            if i == 0:
                value = suffixProducts[i + 1]
            elif i == lenOfNums-1:
                value = prefixProducts[i - 1]
            else:
                value = prefixProducts[i - 1] * suffixProducts[i + 1]
            returnArray.append(value)
        print(returnArray)
        return returnArray