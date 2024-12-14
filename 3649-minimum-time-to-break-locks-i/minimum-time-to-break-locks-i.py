from itertools import permutations
import math
class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        c = permutations(strength)
        som = 10**18
        for l in c:
            X,ans = 1,0
            cur = 0
            for item in l:
                u = math.ceil(item/X)
                ans += u
                X += K

            som = min(som,ans)

        return som