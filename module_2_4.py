numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
no_primes = []

from math import sqrt

def is_prime(n):
	for j in range(2, int(sqrt(n)) + 1):
		if n % j == 0:
			return False
	return True

for i in numbers:
	if is_prime(i) and i != 1:
		primes.append(i)
	elif i != 1:
		no_primes.append(i)

print(f'Simple numbers:\n {primes}')
print('-------------------------')
print(f'Not simple numbers:\n {no_primes}')
