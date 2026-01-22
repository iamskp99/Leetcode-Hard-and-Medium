class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mini,maxi = 0,0
        d,v = indexDifference,valueDifference
        for i in range(d,len(nums)):
            if nums[i-d] < nums[mini]:
                mini = i-d

            if nums[i-d] > nums[maxi]:
                maxi = i-d

            if abs(nums[i]-nums[mini]) >= v:
                return [mini,i]

            if abs(nums[i]-nums[maxi]) >= v:
                return [maxi,i]

        return [-1,-1]