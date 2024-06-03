class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        prev,ans = -1*(10**18),[]
        for i in range(n):
            a = nums[i]
            if a != prev:
                prev,prev2 = a,-1*(10**18)
                j = i+1
                while j < n:
                    b = nums[j]
                    if b != prev2:
                        prev2,prev3,prev4 = b,-1*(10**18),-1*(10**18)
                        val = a+b
                        k,l = j+1,n-1
                        while k < l:
                            if nums[k] == prev3:
                                k += 1
                                continue

                            if nums[l] == prev4:
                                l -= 1
                                continue

                            # prev3,prev4 = nums[k],nums[l]
                            if nums[k]+nums[l]+val == target:
                                prev3 = nums[k]
                                ans.append([a,b,nums[k],nums[l]])
                                k += 1
                                continue

                            if nums[k]+nums[l]+val > target:
                                prev4 = nums[l]
                                l -= 1
                                continue

                            k += 1

                    else:
                        pass
                    j += 1

            else:
                continue

        return ans