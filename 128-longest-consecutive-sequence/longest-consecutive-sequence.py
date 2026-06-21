class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l = list(set(nums))
        s,e = {},{}
        for i in l:
            pele = i-1
            if pele in e:
                start = e[pele]
                e[i] = start
                del e[pele]
                s[start] = i
            else:
                s[i] = i
                e[i] = i

            nele = i+1
            if nele in s:
                end = s[nele]
                e[end] = e[i]
                del e[i]
                del s[nele]
                s[e[end]] = end

        ans = 0
        for i in s:
            ans = max(ans,s[i]-i+1)

        return ans