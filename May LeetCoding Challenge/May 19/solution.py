class StockSpanner:

    def __init__(self):
        self.container = []

    def next(self, price: int) -> int:
        occurance = 1 
        idx  = len(self.container) -1
        while True:
            if idx < 0 : break
            pair = self.container[idx]
            val,occur =  pair[0], pair[1]
            if val <= price :
                occurance += occur
            else :
                break
            idx =  idx - occur

        self.container.append((price,occurance))
        return occurance


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)