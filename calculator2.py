calculation_history = []


def calculate(a, b, operator):
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            return "Ошибка деление на ноль"
        result = a / b
    else:
        return "Неизвестная операция"

    operation_str = F"{a} {operator} {b} = {result}"
    calculation_history.insert(0, operation_str)

    if len(calculation_history) > 3:
        calculation_history.pop()
    return result


def show_history():

    if not calculation_history:
        print("История пуста")
        return
    print("Последнии операции: ")
    for i, operation in enumerate(calculation_history, 1):
        print(F"{i}. {operation}")


if __name__ == "__main__":
    print("=== Умный калькулятор===\n")
print("5 + 3=", calculate(5, 3,'+'))
print("10 / 2 =", calculate(10, 2, '/'))
print("7 * 4 =", calculate(7, 4, '*'))

show_history()

print("\n8 - 2 =", calculate(8, 2, '-'))
show_history()

