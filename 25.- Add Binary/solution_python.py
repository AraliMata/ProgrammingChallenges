class Solution:
    def sumBinary(self, numBin, summ):
        
        if numBin == '111':
            summ += '1'
            numAdd = '1'
        elif numBin == '000':
            summ += '0'
            numAdd = '0'
        elif numBin == '101' or numBin == '110' or numBin == '011':
            summ += '0'
            numAdd = '1'
        elif numBin == '100' or numBin == '010' or numBin == '001':
            summ += '1'
            numAdd = '0'
            
        return summ, numAdd
        
    def addBinary(self, a: str, b: str) -> str:
        
        length = max(len(a), len(b))
        a = a.zfill(length)
        b = b.zfill(length)
        summ = ''
        numAdd = '0'
        
        for i in range(length - 1, -1, -1):
            numBin = a[i] + b[i] + numAdd
            summ, numAdd = self.sumBinary(numBin, summ)
            
        if numAdd == '1':
            summ += '1'
            
        return summ[::-1]
            