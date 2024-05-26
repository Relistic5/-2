import random
first_num = random.randint(3, 20)
numbers = []
second_list = []

# Создаем списки всех цифр от 1 до рандомного
for i in range(first_num):
	numbers.append([])
	for j in range(i):
		numbers[i].append(j+1)


# Функция проверки возможных пар и составления списка с паролем
def check_variations():
	for list_num in range(2, len(numbers)):
		summ = numbers[list_num][0] + numbers[list_num][-1]
		if first_num % summ == 0:
			second_list.append(numbers[list_num][0])
			second_list.append(numbers[list_num][-1])


# Функция удаления первого элемента из списков для дальнейшей проверки
def del_first_elem():
	numbers.pop(0)
	for elem in range(0, len(numbers)):
		numbers[elem].pop(0)


# Повторяем проверки, пока в списках не закончатся элементы
while True:
	if len(numbers) >= 2:
		check_variations()
		del_first_elem()
		continue
	else:
		check_variations()
		break

# Вывод выпавшего числа и пароля к нему
print(f'Выпало число {first_num}')
print('Пароль: ', *second_list, sep='')
