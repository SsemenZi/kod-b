#nomer 1
str = input()
n = list(reversed(str))
print(n)
#nomer 2
str1 = str(input())
n = str(input())
print(str1.replace(n, n*2))
#nemer 3
list1 = input().split()
n = int(input())
list2 =[int(x) ** n for x in list1]
print(list2)
#nomer 4
str = input()
print(str[::2])
#nomer 5
str2 = str(input())
x = str(input())
y = str(input())
k = str2.count(x)
l = str2.count(y)
print(f'x : {k}, y : {l}')
#nomer 6
txt = str(input())
for i in txt:
    if i == ")":
        n = txt.find('(')
        k = txt.find(')')
        m = txt[n:k + 1:]
        txt = txt.replace(m,'')
print(txt)
#nemer 3
list1 = input().split()
n = int(input())
list2 =[int(x) ** n for x in list1]
print(list2)

