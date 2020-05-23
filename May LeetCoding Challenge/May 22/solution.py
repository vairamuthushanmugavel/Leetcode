class Solution:
    def frequencySort(self, s: str) -> str:
        resultstr = []
        count = Counter(s)
        sorted_order = sorted(count.items(), key=lambda count: count[1],reverse=True )
        for i in sorted_order:
            for count in range(i[1]):
                resultstr.append(i[0])
	        # resultstr += i[0] * i[1]
        return "".join(resultstr)