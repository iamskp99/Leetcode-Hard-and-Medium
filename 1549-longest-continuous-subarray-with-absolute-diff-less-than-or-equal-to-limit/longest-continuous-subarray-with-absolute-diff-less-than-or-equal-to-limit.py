from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        queue1,queue2 = deque([]),deque([])
        ans,ind = 1,-1
        for i in range(n):
            x = nums[i]
            if len(queue1) == 0:
                queue1.append(i)
                queue2.append(i)
                continue

            while len(queue1) > 0 and nums[queue1[-1]] < x:
                queue1.pop()

            while len(queue2) > 0 and nums[queue2[-1]] > x:
                queue2.pop()

            queue1.append(i)
            queue2.append(i)
            
            while len(queue1) > 0 and len(queue2) > 0 and abs(nums[queue2[0]]-nums[queue1[0]]) > limit:
                if queue2[0] < queue1[0]:
                    ind = queue2.popleft()
                else:
                    ind = queue1.popleft()
            
            while len(queue1) > 0 and queue1[0] <= ind:
                queue1.popleft()

            while len(queue2) > 0 and queue2[0] <= ind:
                queue2.popleft()

            if len(queue2) > 0 and len(queue1) > 0:
                ans = max(ans,i-ind)

        return ans