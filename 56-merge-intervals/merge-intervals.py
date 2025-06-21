class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i,j,n = 0,1,len(intervals)
        cur_max = intervals[i][1]
        ans = []
        while i < n and j < n:
            if intervals[j][0] > cur_max:
                ans.append((intervals[i][0],cur_max))
                cur_max = intervals[j][1]
                i = j
            else:
                cur_max = max(cur_max,intervals[j][1])
            j += 1

        ans.append((intervals[i][0],cur_max))
        return ans