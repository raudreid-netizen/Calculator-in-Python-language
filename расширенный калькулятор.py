print('''корень - 1 или число в степень - 2 или калькулятор - 3''')
fg = int(input('''операция: '''))
if fg == 1:
	p = int(input("из чего корень:"))
	co=p ** 0.5
	print("число из корня: ",co)
if fg == 2:
	p = int(input("из чего степень:"))
	co=p ** 2
	print("число в стерени: ",co)
if fg == 3:
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