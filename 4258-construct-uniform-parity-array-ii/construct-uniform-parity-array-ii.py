class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minodd,minele = 10**18,10**18
        n = len(nums1)
        for ele in nums1:
            if not ele%2:
                minele = min(minele,ele)
                continue
            minodd = min(minodd,ele)
        
        flag = False
        for i in range(n):
            if nums1[i]%2:
                if minodd == 10**18:
                    flag = True
                    break

                if nums1[i] != minodd and nums1[i] > minodd:
                    continue
                else:
                    flag = True
                    break
        
        if not flag:
            return True

        flag = False
        for i in range(n):
            if not nums1[i]%2:
                if minodd == 10**18 or nums1[i] < minodd:
                    flag = True
                    break
        
        if not flag:
            return True
        return False
        
