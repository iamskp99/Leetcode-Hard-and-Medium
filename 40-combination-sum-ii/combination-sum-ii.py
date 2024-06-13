class Solution:
    def rec(self,ind,candidates,target,now):
        if ind == len(candidates):
            if target == 0:
                cur = [i for i in now]
                self.ans.append(cur)

            return

        if target < 0:
            return 

        if target == 0:
            cur = [i for i in now]
            self.ans.append(cur)
            return

        for i in range(ind,len(candidates)):
            if i > ind:
                if candidates[i] == candidates[i-1]:
                    continue

            now.append(candidates[i])
            self.rec(i+1,candidates,target-candidates[i],now)
            now.pop()
            
        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.rec(0,candidates,target,[])
        return self.ans