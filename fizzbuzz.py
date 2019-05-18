def fizzbuzz(n):
	if type(n) != type(0):
		raise TypeError
	"""
	if not isinstance(n, int):
		raise TypeError("n is not an int")

	if n <= 0:
		raise ValueError("n is not positive")
	"""
	if n % 15 == 0:
		return "fizzbuzz"
	elif n % 3 == 0:
		return "fizz"
	elif n % 5 == 0:
		return "buzz"
		
	return str(n)