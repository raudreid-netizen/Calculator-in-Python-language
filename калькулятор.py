a = int(input("число1: "))
b = int(input("число2: "))

message ='''
+ : Сложение
- : Вычитание
/ : Деление
* : Умножение
'''
operation = input(message)
if operation == '+':
    print('Сложение')
    result = a + b
elif operation == '-':
    print('Вычитание')
    result = a - b
elif operation == '/':
    print('Деление')
    result = a / b
elif operation == '*':
    print('Умножение')
    result = a * b
else:
    print('Неизвестная операция')


print("Результат:", result)