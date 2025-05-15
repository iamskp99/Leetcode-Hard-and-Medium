class Solution:
    
    def longestPalindrome(self, s: str, t: str) -> int:
        #Checks if a string is palindrome or not
        def ispal(s):
            i = 0
            j = len(s)-1
            f = 1
            while i < j:
                if s[i] != s[j]:
                    f = 0
                    break

                i += 1
                j -= 1

            return  f

        l1,l2 = [""],[""]
        n = len(s)
        for i in range(n):
            for j in range(i+1,n+2):
                l1.append(s[i:j])

        n = len(t)
        for i in range(n):
            for j in range(i+1,n+2):
                l2.append(t[i:j])

        ma = 0
        for i in range(len(l1)):
            for j in range(len(l2)):
                x = l1[i]+l2[j]
                if ispal(x):
                    ma = max(ma,len(x))

        return ma

        

                