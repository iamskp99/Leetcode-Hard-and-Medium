class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        if n == 2:
            return 2

        num = len(bin(n)[2:])
        return 2**num

