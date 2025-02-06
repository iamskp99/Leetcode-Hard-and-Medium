class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        mat = [('W','N'),('E','N'),('W','S'),('E','S')]
        ans = 0
        for x in mat:
            cur = [0,0]
            leave = k
            for i in s:
                ele = i
                if ele not in x and leave > 0:
                    if ele in 'EW':
                        ele = x[0]
                    else:
                        ele = x[1]

                    leave -= 1

                if ele == 'N':
                    cur[1] += 1

                if ele == 'S':
                    cur[1] -= 1

                if ele == 'E':
                    cur[0] -= 1

                if ele == 'W':
                    cur[0] += 1
            
                som = abs(cur[0])+abs(cur[1])
                ans = max(ans,som)

        return ans