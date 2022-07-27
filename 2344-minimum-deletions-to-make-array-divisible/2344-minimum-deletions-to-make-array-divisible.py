import math
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        ans = -1
        for i in numsDivide:
            if ans == -1:
                ans = i
                continue
            
            ans = math.gcd(i,ans)
            
        nums.sort()
        cnt = 0
        for i in nums:
            if ans%i == 0:
                return cnt
            
            cnt += 1
            
        return -1