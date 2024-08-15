def get_user_input():
    numbers = input('Введите числа через пробел:\n')
    operation = input('Выберите операцию (1 - сумма, 2 - среднее, 3 - мин/макс, 4 - удалить чётные, 5 - выход):\n')
    return numbers, operation

def summ(numbers):
    split = [int(i) for i in numbers.split()]
    summ= sum(split)
    print ('Сумма всех чисел:', summ)

def average_value(numbers):
    split = [int(i) for i in numbers.split()]
    average_value = sum(split)/len(split)
    print ("Среднее значение:", average_value)

def min_max(numbers):
    split = [int(i) for i in numbers.split()]
    minim = min(split)
    maxim = max(split)
    print("Минимальное значение:", minim, "Максимальное значение:", maxim)

def remove(numbers):
    split = [int(i) for i in numbers.split()]
    removing =  [int(k) for k in split if k%2 != 0]
    string = " ".join(str(removed) for removed in removing)
    print ("Были удалены все числа кратные 2:", string)

numbers, operation = get_user_input()

while True:
    get_user_input()
    if operation == "1":
        summ(numbers)
        break
    elif operation == "2":
        average_value(numbers)
    elif operation == "3":
        min_max(numbers)
    elif operation == "4":
        remove(numbers)
    elif operation == "5":
        print ("Завершение действий")
        break
    else:
        print("Неверная операция! Попробуйте снова.")
    