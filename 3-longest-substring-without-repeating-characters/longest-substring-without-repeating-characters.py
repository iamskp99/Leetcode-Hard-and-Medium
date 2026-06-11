class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,n = 0,0,len(s)
        ch = {}
        ans = 0
        while j < n:
            c = ord(s[j])
            if c in ch and ch[c] > -1:
                i = ch[c]+1
                for k in ch:
                    if ch[k] < i:
                        ch[k] = -1

            ch[c] = j
            ans = max(ans,j-i+1)
            j += 1

        return ans