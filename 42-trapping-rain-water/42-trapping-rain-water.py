class Solution:
    def trap(self, height: List[int]) -> int:
        l,r,ans = [],[],0
        n = len(height)
        ma = 0
        for i in range(n):
            l.append(ma)
            ma = max(ma,height[i])
            
        ma,i = 0,n-1
        while i > -1:
            r.append(ma)
            ma = max(height[i],ma)
            i -= 1
            
        r = r[::-1]
        for i in range(n):
            x = height[i]
            h = min(l[i],r[i])
            if h <= x:
                continue
                
            ans += (h-x)
            
        return ans