class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []
        ele = set()
        i = len(nums)-1
        n = len(nums)
        while i > -1:
            x = nums[i]
            flag = 0
            while len(stack) > 0:
                if x < stack[-1]:
                    flag = 1
                    break

                else:
                    stack.pop()
            
            stack.append(x)
            if len(stack) == 3:
                return True

            if flag:
                ele.add(i)
            i -= 1

        stack = []
        for i in range(n):
            x = nums[i]
            flag = 0
            while len(stack) > 0:
                if x > stack[-1]:
                    flag = 1
                    break

                else:
                    stack.pop()
            
            stack.append(x)
            if flag:
                if i in ele:
                    return True

            if len(stack) == 3:
                return True

        return False
