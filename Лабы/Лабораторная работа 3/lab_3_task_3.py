b = int(input("выберите способ чтения. 1 - построчное чтение, 2 - чтение всего файла сразу "))

try:      #прочерка на существование      
	if b == 1: #построчное чтение
		file = open(r"несуществующийФайл", "r", encoding="utf-8")
		for line in file:
			print(line.strip())
	
	if b == 2:   #чтение всего файла сразу
		a = open(r"несуществующийфайл", "r", encoding="utf-8")
		print(a.read())
except:     
	FileNotFoundError
	print("Файла не существует!")
	
