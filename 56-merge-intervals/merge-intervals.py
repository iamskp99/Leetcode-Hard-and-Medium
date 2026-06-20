class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for ele in intervals:
            if len(ans) == 0:
                ans.append(ele)
            else:
                if ele[0] > ans[-1][-1]:
                    ans.append(ele)
                else:
                    ans[-1][-1] = max(ans[-1][-1],ele[1])
        return ans