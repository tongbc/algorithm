import sys
import heapq

class TopHeap(object):
    def __init__(self,k):
        self.k = k
        self.data = []

    def push(self,elem):
        if len(self.data)<self.k:
            heapq.heappush(self.data,elem)
        else:
            mini = self.data[0]
            if elem>mini:
                heapq.heapreplace(self.data,elem)

    def topK(self):
        # print(reversed([heapq.heappop(self.data) for x in range(len(self.data))]))
        return [x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]


list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
th = TopHeap(5)
for i in list_num:
    th.push(i)
print(th.topK())
# print (th.topK())
lis = [heapq.heappop(list_num) for _ in range(len(list_num))]
print(lis)
