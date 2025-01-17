class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) < len(str1):
            str1,str2 = str2,str1

        ans = []
        o = []
        # print(str1,str2,"KKK")
        for i in str1:
            o.append(i)
            if len(str1)%len(o) == 0 and len(str2)%len(o) == 0:
                r1 = len(str1)//len(o)
                r2 = len(str2)//len(o)
                # print(o,str1,str2)
                cc = "".join(o)
                t1 = cc*r1
                t2 = cc*r2
                if t1 == str1 and t2 == str2:
                    ans = o.copy()

        return "".join(ans)
        