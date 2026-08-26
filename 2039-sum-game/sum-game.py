class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        hn = n//2
        s = num
        s1,s2 = s[0:hn],s[hn:n]
        som1,som2 = 0,0
        q1,q2 = 0,0
        for ele in s1:
            if ele != '?':
                som1 += int(ele)
            else:
                q1 += 1

        for ele in s2:
            if ele != '?':
                som2 += int(ele)
            else:
                q2 += 1

        if q1 == q2:
            if som1 == som2:
                return False

            return True

        if q1 > q2:
            q1,q2 = q2,q1
            som1,som2 = som2,som1

        if som2 > som1:
            return True
        
        diff = abs(som2-som1)
        qdiff = abs(q2-q1)
        if (qdiff//2)*9 == diff and not qdiff%2:
            return False

        # ?329 5???     14 5


        # xxxx 9 9 
        # xxxxx
        
        return True
