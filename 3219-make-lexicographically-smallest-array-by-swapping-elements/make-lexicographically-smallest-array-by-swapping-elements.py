class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        ans = [-1 for i in range(n)]
        l = []
        for i in range(n):
            l.append((nums[i],i))

        l.sort()
        ind,cur = [],[]
        for ele in l:
            # print(ind)
            a,b = ele
            if len(cur) == 0:
                cur.append(a)
                ind.append(b)
            else:
                if a-cur[-1] > limit:
                    ind.sort()
                    for j in range(len(ind)):
                        ans[ind[j]] = cur[j]
                    ind = [b]
                    cur = [a]
                else:
                    cur.append(a)
                    ind.append(b)

        ind.sort()
        for j in range(len(ind)):
            ans[ind[j]] = cur[j]
        return ans
        