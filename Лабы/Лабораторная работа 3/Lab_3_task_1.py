b = int(input("выберите способ чтения. 1 - построчное чтение, 2 - чтение всего файла сразу "))

if b == 1: #построчное чтение
	file = open(r"example.txt", "r", encoding="utf-8")
	for line in file:
		print(line.strip())

if b == 2: #Чтение всего файла сразу
	a = open(r"example.txt", "r", encoding="utf-8")
	print(a.read())
2