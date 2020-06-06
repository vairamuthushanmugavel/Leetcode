class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum =[]
        sum =0 
        for weight in w:
            sum += weight
            self.prefix_sum.append(sum)
        self.totalsum = sum

    def pickIndex(self) -> int:
        rand =  random.random() * self.totalsum
        low,high =  0 , len(self.prefix_sum)
        for i in range(len(self.prefix_sum)):
             if randIdx < self.prefix_sum[i]:
                 return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()