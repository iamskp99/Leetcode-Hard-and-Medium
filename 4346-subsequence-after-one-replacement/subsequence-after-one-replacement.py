class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        # Check if the subsequence can be made without replacement
        if len(t) < len(s):
            return False

        d = {}
        i,j,n,m = 0,0,len(s),len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                d[i] = j
                i += 1
            j += 1
        
        if i == n:
            return True

        i,j = n-1,m-1
        print(d)
        while j > -1 and i > -1:
            if s[i] == t[j]:
                i -= 1
                if i-1 in d and d[i-1] < j-1:
                    print("HII_1",i+1,i-1,d[i-1])
                    return True
                elif i-1 < 0 and j-1 > -1:
                    print("HII_2",i+1)
                    return True
            else:
                if i-1 in d and d[i-1] < j:
                    print("HII_3",i+1)
                    return True
                elif i-1 < 0:
                    print("HII_4",i+1)
                    return True
            j -= 1
        return False
