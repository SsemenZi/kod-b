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
list1 = input().split()
list2 = input().split()
list1 = [int(i) for i in list1]
list2 = [int(i) for i in list2]
if (len(list1)) < (len(list2)):
    for i in range(len(list2) - len(list1)):
        list1.append(0)
if (len(list2)) < (len(list1)):
    for i in range(len(list1) - len(list2)):
        list2.append(0)
print(list(map(lambda a, b: a + b, list1, list2)))
