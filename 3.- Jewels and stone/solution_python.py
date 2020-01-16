#Jewels and stones
#You're given strings J representing the types of stones that are jewels,
#and S representing the stones you have.  Each character in S is a type of stone you have.
#You want to know how many of the stones you have are also jewels.
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        number = 0;
        Jlen = len(J)
        Slen = len(S)
        
        if(Slen > Jlen):
            for i in S:
                for j in J:
                    if(i == j):
                        number += 1
        else:
            for i in J:
                for j in S:
                    if(i == j):
                        number += 1
        
        return number