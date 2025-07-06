class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        return

class LRUCache:

    def __init__(self, capacity: int):
        self.n = capacity
        self.d = {}
        self.count = 0
        self.head = None
        self.last = None
        return
        

    def get(self, key: int) -> int:
        if key in self.d:
            ele = self.d[key]
            if ele == self.head:
                pass
            else:
                pele = ele.prev
                nele = ele.next
                ele.prev = None
                ele.next = None
                pele.next = nele
                ele.next = self.head
                self.head.prev = ele
                self.head = ele
                if nele is None:
                    self.last = pele
                else:
                    nele.prev = pele

            return self.head.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # print(key,self.d)
        if key in self.d:
            ele = self.d[key]
            if ele == self.head:
                ele.val = value
                return

            pele = ele.prev
            nele = ele.next
            ele.prev = None
            ele.next = None
            pele.next = nele
            ele.next = self.head
            self.head.prev = ele
            self.head = ele
            self.head.val = value
            if nele is None:
                self.last = pele
            else:
                nele.prev = pele

        else:
            if self.count == self.n:
                ele = Node(key,value)
                ele.next = self.head
                self.head.prev = ele
                self.head = ele
                self.d[key] = self.head

                now = self.last
                self.last = now.prev
                self.last.next = None
                del self.d[now.key]
            else:
                ele = Node(key,value)
                if self.head is None:
                    self.head = ele
                    self.last = ele
                    self.count += 1
                    self.d[key] = self.head
                    return

                self.head.prev = ele
                ele.next = self.head
                self.head = ele
                self.d[key] = self.head
                self.count += 1

        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)