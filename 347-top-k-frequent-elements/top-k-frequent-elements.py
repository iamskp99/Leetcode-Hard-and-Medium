import sys
input = sys.stdin.readline
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary,cnt = {},[[]]
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1

            else:
                dictionary[i] = 1

            cnt.append([])

        for i in dictionary:
            cnt[dictionary[i]].append(i)

        ans,ptr = [],len(cnt)-1
        while k > 0 and ptr > 0:
            if len(cnt[ptr]) == 0:
                ptr -= 1

            else:
                ans.append(cnt[ptr].pop())
                k -= 1

        return ans