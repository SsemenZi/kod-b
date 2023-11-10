#nomer 1
s = input()
def f(s):
    list1 = []
    list2 = []
    for i in s:
        list1.append(i)
        list2.append(i)
    list2.reverse()
    if list1 == list2:
        print(True)
    else:
        print(False)
f(s)
#nomer 2
fam = input()
ima = input()
ot = input()
god = input()
def f(a, b, c, d):
    print(f'{a} {b} {c} {d} г.р. зарегистрирован')
f(fam, ima, ot, god)
#nomer 3
a = int(input())
b = int(input())
c = 10
def f(a, b, c = 0):
    if a > b and a > c:
        print(f'{a} - наибольшее')
    if b > a and b > c:
        print(b)
    if c > a and c > b:
        print(c)
f(a, b, c)