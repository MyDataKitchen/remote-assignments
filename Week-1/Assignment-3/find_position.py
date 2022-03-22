def find_position(numbers, target):

  for index, num in enumerate(numbers):
    if num == target:
      break

    index = -1

  return index

print(find_position([5, 2, 7, 1, 6], 5)) # should print 0 
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2 
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one) 
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1