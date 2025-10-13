import random

num = random.randint(1, 100)
exit_buttom = False
chis = 0
while not exit_buttom :
    chis = int(input("Введите своё число: "))
    if chis == num :
        exit_buttom = True
    elif chis > num :
        print("Моё число меньше")
    elif chis < num :
        print("Моё число больше")

