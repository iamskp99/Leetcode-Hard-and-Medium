class Solution:
    def powe(self,x,y):
        ans = 1
        c = 1/x
        while y != 0:
            if abs(y)%2:
                if y >= 0:
                    ans = ans*x

                else:
                    ans = ans*c

            if y >= 0:
                y = abs(y)//2
                x = x*x

            else:
                y = abs(y)//2
                y = -1*y
                c = c*c

        return ans
            

    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        return self.powe(x,n)