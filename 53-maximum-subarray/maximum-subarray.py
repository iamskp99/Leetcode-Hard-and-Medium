class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans,som = -1*(10**18),0
        for i in nums:
            ans = max(ans,i)
            if som+i <= 0 or som+i <= i:
                som = i

            else:
                som += i

            ans = max(som,ans)

        return ans