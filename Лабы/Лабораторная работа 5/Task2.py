class Circle():
    """Круг"""

    def __init__(self, radius):
        """Инициализация радиуса круга"""
        self.radius = radius

    def get_radius(self):
        """Возвращение значение радиуса"""
        print("радиус: " + str(self.radius))


    def set_radius(self, new_radius):
        """Изменить радиус"""
        self.radius = new_radius

A = str(input("Введите радиус: "))
Circle1 = Circle(A)
Circle1.get_radius()

B = str(input("Введите новый радиус: "))
Circle1.set_radius(B)

Circle1.get_radius()