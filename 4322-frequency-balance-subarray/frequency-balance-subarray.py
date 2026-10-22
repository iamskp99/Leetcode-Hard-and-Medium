class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        # Prefix Sums ? Nope
        # This can be solved by counting only.
        ans = 0
        for i in range(n):
            d,s = {},set()
            f = {}
            for j in range(i,n):
                x = nums[j]
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1

                if d[x]-1 > 0:
                    f[d[x]-1] -= 1
                    if f[d[x]-1] == 0:
                        del f[d[x]-1]
                        s.remove(d[x]-1)
                
                if d[x] in f:
                    f[d[x]] += 1
                else:
                    f[d[x]] = 1
                    s.add(d[x])

                if len(s) == 1 and len(d) == 1:
                    ans = max(ans,j-i+1)
                elif len(s) == 2:
                    r = []
                    for ele in s:
                        r.append(ele)
                    r.sort()
                    if r[-1] == 2*r[0]:
                        ans = max(ans,j-i+1)
                else:
                    pass

        return ans        
