class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,n = 0,len(height)
        j = n-1
        ans = 0
        aa,bb = 0,0
        while i < j:
            ans = max(ans,min(height[i],height[j])*(j-i))
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                if height[i+1] > height[j-1]:
                    i += 1
                else:
                    j -= 1

        print(aa,bb)
        return ans