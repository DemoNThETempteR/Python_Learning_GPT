a = float(input("Введите первое число:\n"))
b = float(input("Введите второе число:\n"))
c = input("Выберите операцию (+, -, *, /):\n")

if c == "+":
    e = a + b
elif c == "-":
    e = a - b
elif c == "*":
    e = a * b
elif c == "/":
    if b == 0:
        print("Нельзя делить на ноль")
        e = None
    else:
        e = a / b
else:
    e = None
    print("Неправильный оператор")

if e is not None:
    print("Результат:", e)