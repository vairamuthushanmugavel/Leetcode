class Solution:
    def grayCode(self, n: int) -> List[int]:
        def finddecimal(num):
            binary = format(num,"b")
            greycode = binary[0]
            for idx in range(1,len(binary)):
                greycode = greycode + str(int(binary[idx]) ^int(binary[idx-1]))
            
            return int(greycode,2)
        output = []
        rag = pow(2,n)
        for num in range(rag):
            output.append(finddecimal(num))
        return output
        