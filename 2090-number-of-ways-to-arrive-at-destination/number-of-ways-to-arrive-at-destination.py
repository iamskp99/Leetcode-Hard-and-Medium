M = (10**9)+7
class Solution:
    def getmin(self,s):
        e = 10**18
        x = -1
        for i in s:
            if i[0] < e:
                e = i[0]
                x = i

        return x

    def dijkstra(self,v,dist,graph,price,nom,s):
        s.add((0,v))
        dist[v] = 0
        nom[v] = 1
        while len(s) != 0:
            e = self.getmin(s)
            u = e[1]
            s.remove(e)
            if u not in graph:
                continue

            for i in graph[u]:
                v = i
                w = price[(u,v)]
                if dist[v] > dist[u]+w:
                    if dist[v] != 10**18:
                        s.remove((dist[v],v))

                    nom[v] = nom[u] 
                    dist[v] = dist[u]+w
                    s.add((dist[v],v))
                
                elif dist[v] == dist[u]+w:
                    nom[v] = (nom[v]+nom[u])%M

        return

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        dist,nom = [],[]
        for i in range(n+1):
            dist.append(10**18)
            nom.append(0)

        s = set()
        graph = {}
        price = {}
        for x in roads:
            u,v,cost = x[0],x[1],x[2]
            if u in graph:
                graph[u].add(v)
            else:
                graph[u] = {v}

            if v in graph:
                graph[v].add(u)
            else:
                graph[v] = {u}

            price[(u,v)] = cost
            price[(v,u)] = cost

        self.dijkstra(0,dist,graph,price,nom,s)
        # print(dist,nom)
        return nom[n-1]
