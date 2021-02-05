def equalizeArray(arr):
    frequency = {}
    min_del = 0
    for number in arr:
        frequency[number] = frequency.get(number, 0) + 1
    
    values = frequency.values()
    max_freq = max(values)
    for value in values:
        if value != max_freq:
            min_del += value
    
    return min_del

if __name__ == '__main__':
    arr = [3,3,2,1,3]

    print(equalizeArray(arr))