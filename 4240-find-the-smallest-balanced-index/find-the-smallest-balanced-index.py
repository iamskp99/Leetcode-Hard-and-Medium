import heapq
class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        som,n = sum(nums),len(nums)
        h = [1]
        heapq.heapify(h)
        i,ans = n-1,-1
        while i > -1:
            som -= nums[i]
            pr = 1
            while len(h) > 0:
                pre = heapq.heappop(h)
                pr = pr*pre
                if pr > som:
                    break
            
            heapq.heappush(h,pr)
            heapq.heappush(h,nums[i])
            if som == pr:
                ans = i
                break
            
            
            i -= 1

        return ans

        