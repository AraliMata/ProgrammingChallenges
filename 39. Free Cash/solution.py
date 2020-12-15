def repeatedHour():
    n = int(input())
    hours = []
    repeatedHours = [1, 1]

    for i in range(n):
        temp = input()
        if temp in hours:
            repeatedHours[0] += 1
            if repeatedHours[0] > repeatedHours[1]:
                repeatedHours[1] = repeatedHours[0]
        else:
            hours.append(temp)
            repeatedHours[0] = 1 
    return repeatedHours[1]

def numberCashers():
    print(repeatedHour())


if __name__ == "__main__":
    numberCashers()
