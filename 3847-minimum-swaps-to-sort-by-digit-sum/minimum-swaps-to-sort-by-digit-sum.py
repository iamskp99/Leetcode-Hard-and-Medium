class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        l = []
        for i in range(n):
            x = nums[i]
            d = str(x)
            som = 0
            for ele in d:
                som += int(ele)

            l.append((som,x,i))

        l.sort()
        ans = 0
        visited = set()
        for i in range(n):
            x = nums[i]
            while i not in visited:
                if nums[i] == l[i][1]:
                    visited.add(i)
                    break

                ans += 1
                j = l[i][2]
                nums[i],nums[j] = nums[j],nums[i]
                visited.add(i)
                i = j

        return ans