x = int(input())
y = int(input())
def max_of_two(x, y):
	if x>y:
		return x
	elif x==y:
		return "Числа равны"
	else:
		return y

print(max_of_two(x, y))
