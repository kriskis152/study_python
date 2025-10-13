chis = int(input("Введите число: "))

for i in range(2, chis) :
    if i == 2:
       print(i)
    if i % 2 == 0:
     continue
    print(i)