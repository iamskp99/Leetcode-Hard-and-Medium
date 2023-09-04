class Solution:
    def minimumOperations(self, num: str) -> int:
        ans = len(num)
        count = num.count('0')
        ans -= count
        num = num[::-1]
        l = ["57","52","00","05"]
        for x in l:
            cnt,i = 0,0
            for j in num:
                if j == x[i]:
                    i += 1

                else:
                    cnt += 1

                if i == 2:
                    break

            if i == 2:
                ans = min(ans,cnt)

        return ans        