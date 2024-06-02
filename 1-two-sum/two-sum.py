class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cur = []
        for i in range(len(nums)):
            cur.append((nums[i],i))

        cur.sort()
        nums = cur
        n = len(nums)
        for i in range(n):
            low = i+1
            high = n-1
            while low <= high:
                mid = (low+high)//2
                if nums[i][0]+nums[mid][0] == target:
                    return [nums[i][1],nums[mid][1]]

                if nums[i][0]+nums[mid][0] < target:
                    low = mid+1

                else:
                    high = mid-1

        return [-1,-1]