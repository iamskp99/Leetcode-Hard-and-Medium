class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        nums = height
        i,ele = 0,0
        pr,sf = [],[]
        while i < n:
            cur = nums[i]
            if len(pr) == 0:
                pr.append(ele)
                ele = max(ele,cur)
            else:
                pr.append(ele)
                ele = max(ele,cur)
            i += 1

        ele = 0
        i = n-1
        while i > -1:
            cur = nums[i]
            if len(sf) == 0:
                sf.append(ele)
                ele = max(cur,ele)
            else:
                sf.append(ele)
                ele = max(ele,cur)
                
            i -= 1

        sf = sf[::-1]
        ans = 0
        # print(pr,sf)
        for i in range(n):
            if i == 0 or i == n-1:
                continue

            if pr[i] <= nums[i] or sf[i] <= nums[i]:
                continue
            
            count = min(pr[i],sf[i])-nums[i]
            # print(i,count)
            ans += count

        return ans


