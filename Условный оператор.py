x = -8

print('дратути!')
if x < 0:
	print('Меньше нуля')
print('дотвидания')

# примеры
a, b = 10, 5

if a > b:
	print('a > b')

if a > b and a > 0:
	print('success')

if (a > b) and (a > 0 or b < 1000):
	print('success')

if 5 < b and b < 10:  # Некорректное условие. Логично оставить только правую часть..
	print('success')

# Можно сравнивать

if '34' > '123':
	print('success')  # Не совсем понятно, как он сравнивает строки и почему программа решила, что условие верно.. Поднимем этот вопрос на вебинаре.

if '123' > '12':
	print('success')

if [1, 2] > [1, 1]:
	print('success')

# нельзя сравнивать

if '6' > 5:
	print('success')

if [5, 6] > 5:
	print('success')

if '6' != 5:
	print('success')
