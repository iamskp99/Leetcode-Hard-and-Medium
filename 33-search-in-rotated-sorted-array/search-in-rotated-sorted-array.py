class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find Pivot
        pivot,n,ind = 0,len(nums),-1
        if nums[0] > nums[-1]:
            low,high = 0,n-1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] < nums[mid-1]:
                    pivot = mid
                    break

                if nums[mid] < nums[high]:
                    high = mid-1

                else:
                    low = mid+1

        if pivot != 0:
            low,high = 0,pivot-1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    low = mid+1

                else:
                    high = mid-1

        low,high = pivot,n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid+1

            else:
                high = mid-1

        return ind

            