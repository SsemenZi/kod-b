#nomer 1
n = int(input())
m = input().split()
max = 0
for i in m:
    x = (m.count(i)-1)
    if x > 0:
        max += 1
print(max)
#nomer 3
str1 = input().split()
str2 = input().split()
s = set()
x = s.update(str1)
x = s.update(str2)
if x == None:
    print('Anagramma')
#nomer 4
str1 = set(input().split())
str2 = set(input().split())
str3 = set(input().split())
inter = str1.intersection(str2)
inter = str2.intersection(str3)
s = sorted(list(inter))
print(' '.join(s))
#nomer 2
s =  input().split()
s[0] = s[0].capitalize()
print(s)
for i in s:
    for m in i:
        if m == "." or m == "!" or "?":
            index = s.index(i) + 1
            s[index] = s[index].capitalize()
print(' '.join(s))
#nomer 5 ???
s =  input().split()
s[0] = s[0].capitalize()
print(s)
for i in s:
    for m in i:
        if m == "." or m == "!" or "?":
            index = s.index(i) + 1
            s[index] = s[index].capitalize()
print(' '.join(s))
