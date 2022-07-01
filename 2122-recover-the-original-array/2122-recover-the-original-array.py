class Solution:
    def check(self,nums,g,k):
        res = []
        for i in nums:
            if g[i] == 0:
                continue
                
            r = i+k
            e = r+k
            if e not in g:
                return []
            
            if g[e] == 0:
                return []
            
            g[i] -= 1
            g[e] -= 1
            res.append(r)
            
        return res
            
    
    def recoverArray(self, nums: List[int]) -> List[int]:
        #Finding the pairs
        nums.sort()
        n = len(nums)
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
                
            else:
                d[i] = 1
        
        for i in range(1,n):
            x = nums[0]
            y = nums[i]
            if ((x+y)%2) == 1:
                continue
                
            a = (x+y)//2
            k = y-a
            if k <= 0:
                continue
                
            #This is the potential value of k
            g = d.copy()
            ans = self.check(nums,g,k)
            if len(ans) == 0:
                continue
               
            # print(k)
            return ans