class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        new_text = text.split() 
        answer = []
        
        for i in range(2, len(new_text)):
            if(new_text[i - 1] == second and new_text[i - 2] == first):
                answer.append(new_text[i])
                
        return answer