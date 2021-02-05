
def getMoneySpent(keyboards, drives, b):
    keyboards.sort(reverse= True)
    drives.sort(reverse= True)
    max_price = 0
    
    for keyboard in keyboards:
        for drive in drives:
            price = keyboard + drive 
            if max_price < price <= b:
                max_price = price
                
    
    return max_price if max_price != 0 else -1

if __name__ == '__main__':
    b = 10
    keyboards = [3,1]
    drives = [5,2,8]

    print(getMoneySpent(keyboards, drives, b))