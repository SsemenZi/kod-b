#nomer 3
from functools import reduce
list1 = input().split()
l = [int(i) for i in list1]
num_max = reduce(lambda a, b: a if (a > b) else b, l)
print(num_max)
#nomer 2
l = input().split()
list1 = [int(i) for i in l]
num = list(filter(lambda b: b % 13 == 0 or b % 19 == 0, list1))
print(num)
#nomer 1
list1 = [1, 2, 3, 4, 5]
list2 = [7, 8, 5, 67, 13]
x = list(zip(list1, list2))
print(list(map(lambda i: sum(i), x)))