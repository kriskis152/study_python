chislo1 = 0
chislo2 = 0
dey = 0
res = 0 
exit_buttom = False

history = []
mod = str(0)

while not exit_buttom :
    chislo1 = input("Введите перовое число: ")
    chislo2 = input("Введите второе чило: ")
    dey = input("Введите действие: ")
    
    if dey == "+" :
     res = int(chislo1) + int(chislo2)
     print(F"Ваш ответ:{res}")
     mod = F"{chislo1} + {chislo2} = {res}"
     history.append(mod)
    elif dey == "-" :
     res = int(chislo1) - int(chislo2)
     print(F"Ваш ответ:{res}")
     mod = F"{chislo1} - {chislo2} = {res}"
     history.append(mod)
    elif dey == "*" :
     res = int(chislo1) * int(chislo2)
     print(F"Ваш ответ:{res}")
     mod = F"{chislo1} * {chislo2} = {res}"
     history.append(mod)
    elif dey == "/" :
     res = int(chislo1) / int(chislo2) 
     print(F"Ваш ответ:{res}")
     mod = F"{chislo1} / {chislo2} = {res}"
     history.append(mod)
    elif dey == "Exit" or chislo1 == "Exit" or chislo2 =="Exit": # почему выход срабатывает только на "dey"
     exit_buttom = True
print(history)    


