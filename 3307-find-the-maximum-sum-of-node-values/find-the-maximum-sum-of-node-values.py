class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans1,ans2 = [],[]
        for i in nums:
            ee = i^k
            if ee > i:
                ans2.append((ee-i,i))

            else:
                ans1.append((i-ee,i))

        if len(ans2)%2 == 0:
            som = 0
            for i in ans1:
                som += i[1]

            for i in ans2:
                som += (i[0]+i[1])

            return som

        ans1.sort()
        ans2.sort()
        som = 0
        if len(ans2) == 0:
            for i in ans1:
                som += i[1]

            return som

        if len(ans1) == 0:
            for i in range(1,len(ans2)):
                som += (ans2[i][0]+ans2[i][1])

            som += ans2[0][1]
            return som

        r1,r2 = ans1[0],ans2[0]
        
        for i in range(1,len(ans1)):
            som += ans1[i][1]

        for i in range(1,len(ans2)):
            som += (ans2[i][0]+ans2[i][1])

        gain = r2[0]
        loss = r1[0]
        if gain > loss:
            som += (r1[1]-r1[0])
            som += (r2[0]+r2[1])

        else:
            som += r2[1]
            som += r1[1]

        return som

        