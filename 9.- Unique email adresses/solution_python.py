class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        newEmails = []
        c = 0
        
        for i in emails:
            oneEmail = i.split('@')

            for j in range(len(oneEmail[0])):
        
                if(j < len(oneEmail[0])):
                    if oneEmail[0][j] == '.':
                        oneEmail[0] = oneEmail[0].replace('.', '')
                    if oneEmail[0][j] == '+':
                        oneEmail[0] = oneEmail[0][:j]
                
            newEmails.append(oneEmail[0] + '@' + oneEmail[1])
            oneEmail = []
        
        
        
        return len(set(newEmails))
            