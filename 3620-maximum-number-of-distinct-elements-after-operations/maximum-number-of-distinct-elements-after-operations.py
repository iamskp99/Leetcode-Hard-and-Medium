class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        l,ans = [],0
        nums.sort()
        for i in nums:
            x = i+k
            if len(l) > 0 and l[-1] >= x:
                continue

            if len(l) == 0:
                l.append(i-k)
                ans += 1

            else:
                p = i-k
                if p > l[-1]:
                    l.append(p)
                    ans += 1

                else:
                    c = l[-1]+1
                    l.append(c)
                    ans += 1
        
        return ans