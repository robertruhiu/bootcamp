def prime_num(number):
	result = []
	if not isinstance(number, int):
		raise TypeError
	if number <= 0:
		return "Numbers less than or equal to zero are not allowed!"
	elif number == 1:
		return "One is not considered prime number"
	else:
		for i in range(2, number+1):
			isprime = True
			for j in range(2, i):
				if i%j == 0:
					isprime = False
			if isprime:
				result.append(i)
	return result
