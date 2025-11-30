import sys
input = sys.stdin.readline
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        inc1,dec,inc2 = [],[],[]
        i1,d,i2 = 0,0,0
        ans = -1*(10**17)
        flag = 0
        now = -1*(10**17)
        for i in nums:
            if len(inc1) and len(dec) and len(inc2):
                if inc2[-1] < i:
                    i2 += i
                    inc2.append(i)
                    # print(inc1,dec,inc2,i1+d+i2,"HII")
                    if len(inc1) > 1 and len(inc2) > 0 and len(dec) > 0:
                        som = max(i2,inc2[0])
                        cur = 0
                        if now == -1*(10**17):
                            now = i1
                            for j in range(len(inc1)-2):
                                cur += inc1[j]
                                now = max(now,i1-cur)
                                # ans = max(ans,(i1-cur)+d+som)

                        ans = max(ans,now+d+som)

                elif inc2[-1] == i:
                    i1,d,i2 = i,0,0
                    inc1,dec,inc2 = [i],[],[]
                    now = -1*(10**17)
                else:
                    d = i
                    val = dec[-1]
                    i1,i2 = val+i2,0
                    inc1,dec,inc2 = [val]+inc2,[i],[]
                    now = -1*(10**17)
                # print(i,inc1,dec,inc2,"HII_1")
                continue
            
            if len(inc1) and len(dec):
                if i < dec[-1]:
                    d += i
                    dec.append(i)
                    now = -1*(10**17)
                    continue
                elif i == dec[-1]:
                    i1,d,i2 = i,0,0
                    inc1,dec,inc2 = [i],[],[]
                    now = -1*(10**17)
                else:
                    i2 = i
                    inc2.append(i)
                
                if len(inc1) > 1 and len(inc2) > 0 and len(dec) > 0:
                    # print(inc1,dec,inc2,i1+d+i2,"HII")
                    som = max(i2,inc2[0])
                    cur = 0
                    if now == -1*(10**17):
                        now = i1
                        for j in range(len(inc1)-2):
                            cur += inc1[j]
                            now = max(now,i1-cur)
                            # ans = max(ans,(i1-cur)+d+som)

                    ans = max(ans,now+d+som)
                
                # print(i,inc1,dec,inc2,"HII_2")
                continue

            if len(inc1):
                if i > inc1[-1]:
                    inc1.append(i)
                    i1 += i
                elif i == inc1[-1] or len(inc1) == 1:
                    i1,d,i2 = i,0,0
                    inc1,dec,inc2 = [i],[],[]
                else:
                    dec.append(i)
                    d += i

                # print(i,inc1,dec,inc2,"HII_3")
                now = -1*(10**17)
                continue
            
            i1 = i
            inc1 = [i]

        return ans