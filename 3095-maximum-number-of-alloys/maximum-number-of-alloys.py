class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        low,high = 0,10**10
        ans = -1
        while low <= high:
            mid = (low+high)//2
            flag = 0
            for l in composition:
                now = 0
                for i in range(n):
                    x = l[i]
                    if x > 0:
                        c = cost[i]
                        s = stock[i]
                        needed = mid*x
                        rem = needed-s
                        now += max(0,rem*c)

                if now <= budget:
                    flag = 1
                    break

            if flag:
                ans = mid
                low = mid+1

            else:
                high = mid-1

        return ans