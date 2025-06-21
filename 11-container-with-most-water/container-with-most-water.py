class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        ans = 0
        while i < j:
            som = min(height[i],height[j])*(j-i)
            ans = max(ans,som)
            if height[i] == height[j]:
                if height[i+1] < height[j-1]:
                    j -= 1
                else:
                    i += 1
            else:
                if height[i] < height[j]:
                    i += 1
                else:
                    j -= 1

        return ans