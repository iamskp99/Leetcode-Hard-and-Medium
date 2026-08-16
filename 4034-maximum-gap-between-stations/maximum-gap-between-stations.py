from bisect import bisect_right
class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n,m = len(skill),len(station)
        cstack = [[] for i in range(26)]
        stack = []
        i,j=0,0
        while i < n:
            if skill[i] == station[j]:
                stack.append(j)
                i += 1
            j += 1

        for i in range(m):
            cstack[ord(station[i])-97].append(i)
        
        ans,limit = 0,m
        while len(stack) > 1:
            ans = max(ans,stack[-1]-stack[-2])
            ele = station[stack[-1]]
            l = cstack[ord(ele)-97]
            flag = False
            low,high = 0,len(l)-1
            ind = -1
            while low <= high:
                mid = (low+high)//2
                if l[mid] > stack[-2]:
                    if l[mid] < limit:
                        ind = mid
                        low = mid+1
                        flag = True
                    else:
                        high = mid-1
                else:
                    low = mid+1

            if flag and l[ind] > stack[-2] and l[ind] < limit:
                limit = l[ind]
                ans = max(ans,limit-stack[-2])
            else:
                limit = stack[-1]

            stack.pop()


        return ans
