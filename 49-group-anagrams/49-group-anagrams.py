class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            arr = [0 for i in range(26)]
            for e in x:
                r = ord(e)-97
                arr[r] += 1
                
            u = tuple(arr)
            if u in d:
                d[u].append(x)
                
            else:
                d[u] = [x]
                
        ans = []
        for x in d:
            ans.append(d[x])
            
        return ans