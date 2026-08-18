class Solution:
    def helper(self,nums,k):
        flag,n = 0,len(nums)
        flag = 0
        for i in range(1,n):
            cnt = 0
            if i+k > n:
                break

            for j in range(i,min(n,i+k)):
                if nums[j] == nums[0]:
                    flag = 1
                    break
            
            if flag:
                break

        if not flag:
            return nums[0]
        
        return -1

    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == 1:
            d = {}
            for ele in nums:
                if ele in d:
                    d[ele] += 1
                else:
                    d[ele] = 1
            
            ee = -1
            for ele in d:
                if d[ele] == 1:
                    ee = max(ee,ele)

            return ee
        if k == len(nums):
            return max(nums)
        ans = -1
        ans = max(ans,self.helper(nums,k))
        ans = max(ans,self.helper(nums[::-1],k))

        return ans

        
