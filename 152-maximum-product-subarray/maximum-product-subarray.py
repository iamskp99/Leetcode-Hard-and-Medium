class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        pos = nums[0]
        neg = nums[0]
        for i in range(1,len(nums)):
            # Two Phase Kadane's
            x = nums[i]
            if x < 0:
                pos,neg = neg,pos

            if x*pos < x:
                pos = x
            else:
                pos *= x

            if x*neg > x:
                neg = x
            else:
                neg *= x
            
            ans = max(ans,pos)
            
        return ans