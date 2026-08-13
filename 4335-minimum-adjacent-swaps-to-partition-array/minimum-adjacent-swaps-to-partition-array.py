class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        n,M = len(nums),(10**9)+7
        m,bmh,bml = 0,0,0
        sm,em = -1,-1
        ans = 0
        # Pre-Computation
        for i in range(n):
            x = nums[i]
            if x >= a and x <= b:
                if sm == -1:
                    sm = i
                    em = i
                else:
                    em = i
                m += 1
            elif x > b:
                pass
            elif x < a:
                pass
            else:
                pass

        if sm != -1:

            for i in range(sm,em):
                x = nums[i]
                if x > b:
                    bmh += 1
                elif x < a:
                    bml += 1
                else:
                    pass

                
            # High to to Lows
            h,tl = 0,0
            for i in range(min(em+1,n),n):
                x = nums[i]
                if x < a:
                    som = (bmh+h)%M
                    ans = (ans+som)%M
                    ans = (ans+m)%M
                    tl += 1
                else:
                    h += 1
            
            # Lows to Highs
            j = sm-1
            l = 0
            while j > -1:
                x = nums[j]
                if x > b:
                    som = (bml+l)%M
                    som = (som+tl)%M
                    ans = (ans+som)%M
                    ans = (ans+m)%M
                else:
                    l += 1
                j -= 1
            
            # Middle
            j = em
            tm,tbml=0,0
            while j >= sm:
                x = nums[j]
                if x >= a and x <= b:
                    tm += 1
                elif x > b:
                    ans = (ans+tm)%M
                    ans = (ans+tbml)%M
                elif x < a:
                    tbml += 1
                else:
                    pass
                j -= 1
            
            tm = 0
            for i in range(sm,em):
                x = nums[i]
                if x >= a and x <= b:
                    tm += 1
                elif x > b:
                    pass
                elif x < a:
                    ans = (ans+tm)%M
                else:
                    pass

            return ans
        else:
            # print("AS")
            high = 0
            for i in range(n):
                x = nums[i]
                if x < a:
                    ans = (ans+high)%M
                else:
                    high += 1
            return ans

        
