import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slope_count = defaultdict(int)
            duplicates = 1
            curr_max = 0

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                g = math.gcd(dx, dy)
                dx //= g
                dy //= g

                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    if dx < 0:
                        dx *= -1
                        dy *= -1

                slope_count[(dx, dy)] += 1
                curr_max = max(curr_max, slope_count[(dx, dy)])

            ans = max(ans, curr_max + duplicates)

        return ans