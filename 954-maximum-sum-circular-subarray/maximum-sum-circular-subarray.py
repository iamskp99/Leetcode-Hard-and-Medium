class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        ans,som = nums[0],nums[0]
        minAns,mSom = nums[0],nums[0]
        total += nums[0]
        for ind in range(1,n):
            i = ind
            total += nums[i]
            if nums[i] >= som+nums[i]:
                som = nums[i]
            else:    
                som += nums[i]

            if mSom+nums[i] < nums[i]:
                mSom += nums[i]
            else:
                mSom = nums[i]

            minAns = min(mSom,minAns)
            ans = max(som,ans)

        if total == minAns:
            return ans
        
        return max(ans,total-minAns)