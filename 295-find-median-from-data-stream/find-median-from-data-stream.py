import heapq
class MedianFinder:

    def __init__(self):
        self.h1,self.h2 = [],[]
        heapq.heapify(self.h1)
        heapq.heapify(self.h2)

    def addNum(self, num: int) -> None:
        if len(self.h1) == 0 and len(self.h2) == 0:
            heapq.heappush(self.h2,num)
            return

        if len(self.h2) == len(self.h1):
            v1 = -1*self.h1[0]
            if v1 > num:
                heapq.heappop(self.h1)
                heapq.heappush(self.h1,-1*num)
                heapq.heappush(self.h2,v1)

            else:
                heapq.heappush(self.h2,num)

            return 

        v1 = self.h2[0]
        if num < v1:
            heapq.heappush(self.h1,-1*num)
            return 

        heapq.heappop(self.h2)
        heapq.heappush(self.h2,num)
        heapq.heappush(self.h1,-1*v1)
        return 

    def findMedian(self) -> float:
        if len(self.h2) != len(self.h1):
            return self.h2[0]

        return ((-1*self.h1[0])+self.h2[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()