class Book():
    """Описание книги"""

    def __init__(self, title, author, year):
        """Атрибуты книги"""
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        """Информация о книге"""
        print("Название книги: " + self.title + ", автор: " + self.author + ", год издания: " + str(self.year))

Book1 = Book("Мастер и Маргарита", "Михаил Афанасьевич Булгаков", 2021)
Book1.get_info()