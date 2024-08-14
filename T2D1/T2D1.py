def get_user_input():
    text = input('Введите текст:\n')
    operation = input('Выберите операцию (1 - подсчет слов, 2 - подсчет символов, 3 - инверсия строки, 4 - замена пробелов):\n')
    return text, operation

def count_words(text):
    words = text.split()
    print("Количество слов:", len(words))

def count_characters(text):
    print("Количество символов:", len(text))

def reverse_text(text):
    print("Инвертированная строка:", text[::-1])

def replace_spaces(text):
    print("Текст с замененными пробелами:", text.replace(" ", "_"))

text, operation = get_user_input()

if operation == "1":
    count_words(text)
elif operation == "2":
    count_characters(text)
elif operation == "3":
    reverse_text(text)
elif operation == "4":
    replace_spaces(text)
else:
    print("Неверная операция! Попробуйте снова.")