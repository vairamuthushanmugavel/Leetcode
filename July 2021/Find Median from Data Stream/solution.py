from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = SortedList()
        

    def addNum(self, num: int) -> None:
        self.container.add(num)
        

    def findMedian(self) -> float:
        length = len(self.container)
        if (length%2) == 0:
            idx = length//2
            return (self.container[idx] + self.container[idx-1])/2
        else:
            return self.container[length//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()