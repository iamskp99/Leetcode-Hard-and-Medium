class Solution:
    def is_pal(self,x):
        i = 0
        j = len(x)-1
        while i < j:
            if x[i] != x[j]:
                return False

            i += 1
            j -= 1

        return True

    def rec(self,i,l):
        if i >= len(self.s):
            flag = 0
            for x in l:
                if self.is_pal(x):
                    pass

                else:
                    flag = 1

            if flag:
                return 

            self.ans.append(l)
            return 

        c,a = self.s[i],""
        p1 = l[:]
        p2 = l[:]
        if len(p1) > 0:
            a = p1.pop()
        
        a = a+c
        p1.append(a)
        p2.append(c)
        self.rec(i+1,p1)
        if len(l) > 0:
            self.rec(i+1,p2)
            
        return

    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.s = s
        self.rec(0,[])
        return self.ans