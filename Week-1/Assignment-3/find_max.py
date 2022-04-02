def find_max(numbers):
    
    temp = numbers[0]
    
    for num in numbers:
        if num > temp:
            temp = num

    return temp


print(find_max([1, 2, 4, 5])); 
print(find_max([5, 2, 7, 1, 6])); 