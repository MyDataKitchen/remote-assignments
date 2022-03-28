def binary_search_position(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
      mid = (left + right) // 2

      if numbers[mid] < target:
        left = mid + 1

      elif numbers[mid] > target:
        right = mid - 1

      else:
        return mid

    return -1


print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3