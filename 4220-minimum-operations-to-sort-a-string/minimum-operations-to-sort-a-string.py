class Solution:
    def minOperations(self, s: str) -> int:
        ts = "".join(sorted(list(s)))
        if s == ts:
            return 0

        if len(s) == 2:
            return -1

        mif,maf = 0,0
        for i in s:
            if i == ts[0]:
                mif += 1
            if i == ts[-1]:
                maf += 1
        
        if s[0] == ts[0] or s[-1] == ts[-1]:
            return 1

        if s[0] == ts[-1] and s[-1] == ts[0]:
            if mif > 1 or maf > 1:
                return 2
            return 3

        return 2