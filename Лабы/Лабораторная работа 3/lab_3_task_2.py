a = str(input())
file = open(r"user_input.txt", "a+", encoding="utf-8")
file.write(a)  #запись в файл текста с сохранением предыдущего содержимого
file.read()
