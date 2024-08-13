def scan():
    a = input ('Введите текст:' + '\n')
    b = input ('Выберите операцию (1 - подсчет слов, 2 - подсчет символов, 3 - инверсия строки, 4 - замена пробелов):' + '\n')
    return a, b

def split():
    y = a.split()
    return y

def summ():
   c = len(y)
   return c

def replace():
    g = a.replace(" ", '_')
    return g
   
a, b = scan()
y = split()
c = summ()
g = replace()
print (g)