exit_buttom = False
res = int(0) 
res1 = int(0)
schet = int(0)
max1 = int(0)
min1 = int(0)
while not exit_buttom :
    res = int(input("Введите число: "))
    if res != 0 :
     res1 = res1 + res
     schet = schet + 1
     if res > max1 :
        max1 = res
     elif res < min1 :
       min1 = res
    elif res == 0 :
       exit_buttom = True
sred = int(res1 / schet)       
print(F"Колличество чисел: {schet}, сумма: {res1}, максимальное: {max1}, минимальное: {min1}, среднее: {sred}")


    