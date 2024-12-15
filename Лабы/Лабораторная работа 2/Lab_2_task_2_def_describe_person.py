name = str(input("Как вас зовут: "))

def describe_person(name, age = 30):
	return f"Меня зовут {name}, мне {age} лет."
print(describe_person(name, age = 30))
