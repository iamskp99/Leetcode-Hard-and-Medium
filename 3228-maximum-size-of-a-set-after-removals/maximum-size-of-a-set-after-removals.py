class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = len(set(nums1))
        s2 = len(set(nums2))
        c = len(set(nums1)&set(nums2))
        n = len(nums1)
        return min(n,min(n//2,s1-c)+min(n//2,s2-c)+c)