def binary_search_first(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
      mid = (left + right) // 2

      if numbers[mid] < target:
        left = mid + 1

      elif numbers[mid] >= target:
        right = mid - 1
  
    return left

 
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2)) # should print 1 (the index of the target number ‘2’)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5)) # should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3)) # should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger then 3', that is, the index of the ‘first’ number 5)