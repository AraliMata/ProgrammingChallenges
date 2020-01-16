#Defanging an IP addrees
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address1 = ""
        for i in address:
            if i == ".":
                address1 += "[.]"
            else:
                address1 += i
        
            
        return address1