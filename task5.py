chislo1 = int(0)
chislo2 = int(0)
dey = 0
res = 0 
exit_buttom = False

while not exit_buttom :
    chislo1 = input("Введите перовое число: ")
    chislo2 = input("Введите второе чило: ")
    dey = input("Введите действие: ")
    
    if dey == "+" :
     res = chislo1 + chislo2
     print(F"Ваш ответ:{res}")
    elif dey == "-" :
     res = chislo1 - chislo2
     print(F"Ваш ответ:{res}")
    elif dey == "*" :
     res = chislo1 * chislo2
     print(F"Ваш ответ:{res}")
    elif dey == "/" :
     res = chislo1 / chislo2 
     print(F"Ваш ответ:{res}")
    elif dey == "Exit" :
     exit_buttom = True


