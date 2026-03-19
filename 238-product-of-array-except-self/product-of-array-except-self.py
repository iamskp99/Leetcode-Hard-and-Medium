class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans,result = 1,[]
        zero = 0
        without_zero = 1
        for x in nums:
            ans = ans*x
            if x == 0:
                zero += 1
            else:
                without_zero = without_zero*x

        if zero == 0:
            result = [ans//x for x in nums]
        else:
            if zero > 1:
                result = [0 for i in range(len(nums))]
            else:
                result = []
                for x in nums:
                    if x == 0:
                        result.append(without_zero)
                    else:
                        result.append(0)
        return result