class Solution:
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        parray,sarray = [],[]
        diff = 10**18
        for i in range(n):
            if i == 0:
                parray.append(0)
            else:
                if diff == 10**18:
                    diff = nums[i]-nums[i-1]
                    parray.append(1)
                elif nums[i]-nums[i-1] == diff:
                    parray.append(parray[-1]+1)
                else:
                    diff = nums[i]-nums[i-1]
                    parray.append(1)

            # print(i,parray)
        
        ans = 2
        i,diff = n-1,10**18
        while i > -1:
            if i == n-1:
                sarray.append(0)
            else:
                if diff == 10**18:
                    diff = nums[i]-nums[i+1]
                    sarray.append(1)
                elif nums[i]-nums[i+1] == diff:
                    sarray.append(sarray[-1]+1)
                else:
                    diff = nums[i]-nums[i+1]
                    sarray.append(1)
                # print(sarray)
            i -= 1

        sarray = sarray[::-1]
        # print(parray)
        # print(sarray)
        for i in range(n):
            if i == 0 or i == n-1:
                ans = max(parray[i]+1,sarray[i]+1,ans)
                continue

            ans = max(parray[i]+1,sarray[i]+1,ans)
            ans = max(ans,parray[i]+2,sarray[i]+2)
            flag = True
            if (nums[i+1]-nums[i-1])/2 == (nums[i+1]-nums[i-1])//2:
                dd = (nums[i+1]-nums[i-1])//2
                curr = 3
                flag = 0
                if i+2 < n:
                    if nums[i+2]-nums[i+1] != dd:
                        curr -= 1
                        flag += 1

                if i-2 >= 0:
                    if nums[i-1]-nums[i-2] != dd:
                        curr -= 1
                        flag += 1

                if flag < 2:
                    cur = sarray[i+1]+parray[i-1]+curr
                    ans = max(ans,cur)
                # print(i,"HII",cur,dd,curr)
                    
                
            # print(i,ans)

        return ans

        



        