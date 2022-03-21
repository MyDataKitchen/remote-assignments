def find_max(numbers):
    
    temp = numbers[0]
    
    for num in numbers:
        if num > temp:
            temp = num

    return temp


