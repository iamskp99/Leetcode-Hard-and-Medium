class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0,p1,p2 = -1,-1,-1
        n = len(nums)
        for i in range(n):
            x = nums[i]
            if x == 0:
                p0 += 1
                p1 += 1
                p2 += 1
                nums[p0] = 0
                if p0 != p1:
                    nums[p1] = 1

                if p1 != p2:
                    nums[p2] = 2

            if x == 1:
                p1 += 1
                p2 += 1
                nums[p1] = 1
                if p1 != p2:
                    nums[p2] = 2

            if x == 2:
                p2 += 1
                nums[p2] = 2

        return nums