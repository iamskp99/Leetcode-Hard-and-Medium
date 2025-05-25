import sys
input = sys.stdin.readline
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        d = {}
        ans,ma = [],0
        for i in range(len(groups)):
            ele = groups[i]
            ma = max(ma,ele)
            ans.append(-1)
            if ele in d:
                d[ele].append(i)
            else:
                d[ele] = [i]
        
        prev = set()
        for i in range(len(elements)):
            ele = elements[i]
            if ele in prev:
                continue
            for j in range(1,(10**5)+2):
                val = ele*j
                if val > ma:
                    break

                if val in d:
                    for x in d[val]:
                        ans[x] = i

                    del d[val]

            prev.add(ele)

        return ans

        