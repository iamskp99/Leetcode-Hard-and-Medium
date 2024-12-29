class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        ans = 0
        for i in range(n):
            for j in range(i+2,n):
                gc = gcd(nums[i], nums[j])
                e1 = nums[i] // gc
                e2 = nums[j] // gc
                key = (e1, e2)
                if key in d:
                    d[key].append(j)

                else:
                    d[key] = [j]

        for ele in d:
            d[ele].sort()
        p = n - 1
        while p >= 0:
            q = p + 2
            while q < n:
                gc = gcd(nums[p], nums[q])
                e1 = nums[q] // gc
                e2 = nums[p] // gc
                key = (e1, e2)
                if key in d:
                    curArr = d[key]
                    lowerBoundIndex = bisect.bisect_left(curArr, p - 1)
                    ans += (lowerBoundIndex)
                    
                else:
                    pass
                q += 1
            p -= 1
        return ans