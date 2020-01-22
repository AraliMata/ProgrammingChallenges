class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        #01/01/1971 : Friday
        
        week = {3:'Sunday', 4:'Monday', 5:'Tuesday', 6:'Wednesday', 0:'Thursday', 1:'Friday', 2:'Saturday'}
        months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        numberYear = year - 1971
        numberDays = (numberYear - numberYear // 4) * 365 + numberYear // 4 * 366
        
        if(numberYear % 4 > 1 and numberYear % 4 < 4):
            numberDays += 1
        elif(numberYear % 4 == 1 and month > 2):
            numberDays += 1
            
        for i in range(1, month):
            numberDays += months[i]
    
        nameD = (numberDays + day) % 7
        
        return week[nameD]