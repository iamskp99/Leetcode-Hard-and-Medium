from bisect import bisect_left
class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n,combined = len(costs),[]
        for i in range(n):
            combined.append((costs[i],capacity[i]))
        combined.sort(key= lambda x: (x[0],-x[1]))
        capacity,costs = [],[]
        for i in range(n):
            costs.append(combined[i][0])
            capacity.append(combined[i][1])
        
        pcapacity,mi = [],-1*(10**18)
        for i in range(n):
            mi = max(mi,capacity[i])
            pcapacity.append(mi)

        ans = 0 
        i = n-1
        while i > -1:
            res = capacity[i]
            remaining = budget-costs[i]
            if remaining <= 0:
                pass
            else:
                ans = max(ans,res)
                ind = bisect_left(costs,remaining-1)
                if ind >= i:
                    ind = i-1
                else:
                    if remaining-1 != costs[ind]:
                        ind -= 1
                
                if ind >= i or ind == -1:
                    pass
                else:
                    res += pcapacity[ind]
                    ans = max(ans,res)
            i -= 1

        return ans