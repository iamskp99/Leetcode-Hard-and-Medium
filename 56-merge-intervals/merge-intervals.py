class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans,n = [],len(intervals)
        j = 0
        while j < n:
            if len(ans) == 0:
                ans.append(intervals[j])

            else:
                ele = intervals[j]
                if ele[0] > ans[-1][-1]:
                    ans.append(ele)

                else:
                    ans[-1][-1] = max(ans[-1][-1],ele[1])

                j += 1

        return ans