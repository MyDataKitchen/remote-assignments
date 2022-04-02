def avg(data):
  sum = 0
  for product in data['products']:
    sum += product['price']
  
  return sum


print( avg({"products": [ {"name": "Product 1","price": 100 },{"name": "Product 2", "price": 700}, {"name": "Product 3","price": 300 }] })) # print the average price of all products (round to 3 decimal)