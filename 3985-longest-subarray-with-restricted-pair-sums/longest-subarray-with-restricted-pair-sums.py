class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        i,j = 0,0
        n,ans = len(nums),0
        while j < n:
            x = nums[j]
            pi,d = -1,{}
            # print(j,"HII")
            for a in range(i,j):
                diff = x-nums[a]
                if diff in d:
                    pi = max(pi,d[diff])
                
                if x+nums[a] in d:
                    pi = max(pi,d[x+nums[a]])
                
                if nums[a]-x in d:
                    pi = max(pi,d[nums[a]-x])
                
                d[nums[a]] = a
                # print(d)
            
            i = pi+1 if pi != -1 else i
            res = j-i+1 if pi == -1 else j-i
            # print(res,"J",j,i)
            ans = max(ans,res)
            j += 1

        return ans
