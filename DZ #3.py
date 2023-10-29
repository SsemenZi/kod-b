#Номер один
a = int(input())
print(a // 100 + a % 10 + a % 100 // 10)
#Номер два
n = int(input())
k = 1
for i in range( 1 , n + 1):
    k *= i
print(k)
#НОмер три
n = int(input())
for i in range(7, n + 1):
    if i % 7 == 0:
        print(i)

