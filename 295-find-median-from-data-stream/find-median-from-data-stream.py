import heapq
class MedianFinder:

    def __init__(self):
        self.h1,self.h2 = [],[]
        heapq.heapify(self.h1)
        heapq.heapify(self.h2)

    def addNum(self, num: int) -> None:
        if (len(self.h1)+len(self.h2))%2:
            if len(self.h2) > 0 and self.h2[0] < num:
                heapq.heappush(self.h2,num)
            else:
                if num < -1*self.h1[0]:
                    ele = -1*heapq.heappop(self.h1)
                    heapq.heappush(self.h2,ele)
                    heapq.heappush(self.h1,-1*num)
                else:
                    heapq.heappush(self.h2,num)
                
        else:
            if len(self.h1) == 0:
                heapq.heappush(self.h1,-1*num)
                return 

            if self.h2[0] > num:
                heapq.heappush(self.h1,-1*num)
                # self.h1.append(-1*num)
            else:
                ele = -1*heapq.heappop(self.h2)
                heapq.heappush(self.h1,ele)
                heapq.heappush(self.h2,num)
        

    def findMedian(self) -> float:
        if (len(self.h1)+len(self.h2))%2:
            return -1*self.h1[0]
        else:
            return (-1*self.h1[0]+self.h2[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()