class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i,j,d=0,0,{}
        n,ans = len(nums),1
        while j < n:
            x = nums[j]
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

            if d[x] > k:
                while i <= j and d[x] > k:
                    d[nums[i]] -= 1
                    i += 1
            
            ans = max(ans,j-i+1)
            j += 1

        return ans
