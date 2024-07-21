import sys
sys.setrecursionlimit(10**5)
class Solution:
    def rec(self,l,som,choice):
        # print(l)
        # return 0 
        if len(l) == 0 or choice == 2:
            return 0

        choice = 1 if self.target[l[0]]-(self.nums[l[0]]+som) > 0 else 0
        cnt = 10**18
        ans = 0
        if choice == 1:
            for ele in l:
                cnt = min(self.target[ele]-(self.nums[ele]+som),cnt)
                if cnt == 0:
                    return 0

            o = []
            for ele in l:
                val = self.target[ele]-(self.nums[ele]+som+cnt)
                if val == 0:
                    ans += self.rec(o,som+cnt,1)
                    o = []

                else:
                    o.append(ele)

            ans += self.rec(o,som+cnt,1)

        else:
            for ele in l:
                cnt = min((self.nums[ele]-som)-self.target[ele],cnt)
                if cnt == 0:
                    return 0

            o = []
            for ele in l:
                val = (self.nums[ele]-(som+cnt))-self.target[ele]
                if val == 0:
                    ans += self.rec(o,som+cnt,0)
                    o = []

                else:
                    o.append(ele)

            ans += self.rec(o,som+cnt,0)

        return cnt+ans

    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        self.target,self.nums = target,nums
        prev,n = 1,len(nums)
        o,ans = [],0
        for i in range(n):
            x = target[i]-nums[i]
            if x > 0:
                if prev == 1:
                    o.append(i)

                else:
                    ans += self.rec(o,0,prev)
                    o = [i]

                prev = 1

            elif x == 0:
                if prev == 2:
                    o.append(i)

                else:
                    ans += self.rec(o,0,prev)
                    o = [i]

                prev = 2

            else:
                if prev == 0:
                    o.append(i)
                
                else:
                    ans += self.rec(o,0,prev)
                    o = [i]

                prev = 0

        ans += self.rec(o,0,prev)
        return ans