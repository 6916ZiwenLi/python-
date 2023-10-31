from functools import reduce

lst = [23, 16, 18, 19, 76, 121, 33, 57, 80]

result = reduce(lambda x, y: x * y, lst)

print(result)
