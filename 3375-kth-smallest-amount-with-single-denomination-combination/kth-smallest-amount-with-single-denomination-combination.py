import math
# Binary search

class Solution:
    def helper(self,coins,val):
        n = len(coins)
        nans = 0

        for i in range(1,2**n):
            b = bin(i)[2:][::-1]
            cnt,lcm = 0,1
            for j in range(len(b)):
                if b[j] == '1':
                    lcm = (lcm*coins[j])//math.gcd(lcm,coins[j])
                    cnt += 1

            if cnt % 2 == 1:
                nans += val // lcm
            else:
                nans -= val // lcm
        
        return nans

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        low,high = 0,10**13
        ans = -1
        coins.sort()
        now_coins = []
        for ele in coins:
            flag = 0
            for nele in now_coins:
                if ele%nele == 0:
                    flag = 1
                    break
            if not flag:
                now_coins.append(ele)
        
        coins = now_coins
        while low <= high:
            mid = (low+high)//2
            nans = self.helper(coins,mid)
            if nans >= k:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
