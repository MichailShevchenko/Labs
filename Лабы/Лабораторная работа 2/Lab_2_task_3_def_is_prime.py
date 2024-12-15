number = int(input())

def is_prime(number):
	for n in range(2, number):
		if number%1 == 0 and number%number==0 and number%n!=0:
			return True
		else:
			return False

print(is_prime(number))
