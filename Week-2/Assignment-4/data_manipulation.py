def count(input):
  result = {}
  for char in input: 
    if char in result:
      result[char] += 1 
    else:
      result[char] = 1
  
  return result
    
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

"""
=======================================================================
"""

def group_by_key(input2):

  result = {}
  for dic in input2:
    if dic['key'] in result:
      result[dic['key']] += dic['value']
    else:
      result[dic['key']] = dic['value']

  return result

input2 = [
{'key': 'a', 'value': 3}, 
{'key': 'b', 'value': 1}, 
{'key': 'c', 'value': 2}, 
{'key': 'a', 'value': 3}, 
{'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}