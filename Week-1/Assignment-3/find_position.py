def find_position(numbers, target):
  index = 0
  for num in numbers:
    if num == target:
      return index

    index += 1

  return -1

print(find_position([5, 2, 7, 1, 6], 5)) # should print 0 
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2 
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one) 
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1