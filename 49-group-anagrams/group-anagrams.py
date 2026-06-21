class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for ele in strs:
            u = [0 for i in range(26)]
            for i in ele:
                u[ord(i)-97] += 1

            c = tuple(u)
            if c in d:
                d[c].append(ele)
            else:
                d[c] = [ele]

        ans = []
        for ele in d:
            ans.append(d[ele])
        return ans