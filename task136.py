chis1 = str(input("Введите число: "))
res = 0
num = len(chis1)
chis2 =0

for i in range(0, num) :
 chis2 = int(chis1[i])
 res = res + chis2
 
print(res)