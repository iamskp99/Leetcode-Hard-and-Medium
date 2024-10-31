class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        s = set()
        for x in range(18):
            s.add(2**x)

        for i in nums:
            if i == 2:
                ans.append(-1)

            else:
                if i+1 in s:
                    val = bin(i)[2:]
                    val = "1"+("0"*(len(val)-1))
                    ans.append(int(val,2)-1)

                else:
                    g = bin(i)[2:]
                    j = len(g)-1
                    count = 0
                    while j > -1:
                        x = g[j]
                        if x == '1':
                            count += 1

                        else:
                            break

                        j -= 1

                    ans.append(i-(2**(count-1)))
                
        return ans