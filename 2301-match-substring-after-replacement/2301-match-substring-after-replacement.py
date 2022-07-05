from collections import deque
class Solution:
    def check(self,x,y):
        # print(x,y)
        g = {}
        i = 0
        while i < len(y):
            # print(g)
            if x[i] != y[i]:
                if y[i] not in self.d:
                    return False
                
                if x[i] not in self.d[y[i]]:
                    return False
                
#                 if y[i] in g:
#                     if g[y[i]] != x[i]:
#                         return False
                    
#                 else:
#                     g[y[i]] = x[i]
            
            i += 1
            
        return True
    
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        i,n,m = 0,len(s),len(sub)
        l = deque([])
        self.d = {}
        for q in range(len(mappings)):
            r = mappings[q]
            w1,w2 = r[0],r[1]
            if w1 in self.d:
                self.d[w1].add(w2)
                
            else:
                self.d[w1] = {w2}
                                   
        while i < m:
            z = s[i]
            l.append(z)
            i += 1
        
        o = list(sub)
        if self.check(l,o) == True:
            return True
        
        while i < n:
            e = l.popleft()
            z = s[i]
            l.append(z)
            if self.check(l,o) == True:
                return True
            
            i += 1
        
        return False