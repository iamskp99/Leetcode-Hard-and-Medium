import sys
input = sys.stdin.readline
class Solution:
    def check(self,x):
        d = []
        e = []
        for i in range(26):
            d.append(0)
            e.append(0)

        i = 0
        p = -1
        while i < x:
            ele = ord(self.s[i])-97
            e[ele] += 1
            p = ele
            i += 1

        if e[p] == x:
            d[p] += 1

        j = i
        i = 0
        while j < len(self.s):
            ele = ord(self.s[i])-97
            e[ele] -= 1
            ele = ord(self.s[j])-97
            p = ele
            e[ele] += 1

            if e[p] == x:
                d[p] += 1
                if d[p] == 3:
                    return True
            
            i += 1
            j += 1


        return False

    def maximumLength(self, s: str) -> int:
        n = len(s)
        self.s = s
        low,high,ans = 1,n-2,-1
        while low <= high:
            mid = (low+high)//2
            if self.check(mid):
                ans = mid
                low = mid+1

            else:
                high = mid-1

        return ans