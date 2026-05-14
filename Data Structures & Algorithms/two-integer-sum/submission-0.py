class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #remember the sum so no need to recalculte 3,4 -> 7 and 4,3 = 7 
        prevMap = {} #val -> index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[num] = i
        return prevMap


        

        