class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d,ans = {},[]
        for ele in names:
            if ele in d:
                now = d[ele]+1
                while ele+f"({now})" in d:
                    now += 1

                c = ele+f"({now})"
                d[c] = 0
                d[ele] += 1
                ans.append(c)
            else:
                d[ele] = 0
                ans.append(ele)

        return ans