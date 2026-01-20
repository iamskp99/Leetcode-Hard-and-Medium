class Solution:
    def rec(self,i,parent):
        cost,flag = 0,False
        if i in self.graph:
            for ele in self.graph[i]:
                if ele != parent:
                    cnt,nflag = self.rec(ele,i)
                    if nflag:
                        cost += (1+cnt)
                    flag = nflag|flag

            flag = flag|self.hasApple[i]
            print(i,flag,cost)
            return (cost+1,flag)
        else:
            return (0,False)

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.graph = {}
        self.hasApple = hasApple
        for ele in edges:
            x,y = ele
            if x in self.graph:
                self.graph[x].add(y)
            else:
                self.graph[x] = {y}
            
            if y in self.graph:
                self.graph[y].add(x)
            else:
                self.graph[y] = {x}

        ans = self.rec(0,-1)[0]
        return ans-1 if ans>0 else 0
