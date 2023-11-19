#nomer 1
a = int(input())
b = int(input())
if a >= b:
    i = a
    c = a
i = b
c = b
while (i % a) + (i % b) > 0:
    i += c
print(i)
#nomer 2
n = int(input())
lst = []
for i in range(2, n):
  count = 0
  for j in range(2, int(i ** 0.5) + 1):
    if i % j == 0:
      count += 1
      break
  if count == 0:
      lst.append(i)
print(lst)
#nomer 3
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i)