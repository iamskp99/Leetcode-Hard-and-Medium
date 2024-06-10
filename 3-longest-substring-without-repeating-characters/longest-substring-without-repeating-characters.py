class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind = [-1 for i in range(300)]
        i,j,n,ans = 0,0,len(s),0
        while j < n:
            cur = ord(s[j])
            if ind[cur] == -1 or ind[cur] < i:
                ind[cur] = j
                ans = max(j-i+1,ans)
                j += 1
                continue

            i = ind[cur]+1

        return ans
            