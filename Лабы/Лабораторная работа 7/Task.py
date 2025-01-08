class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Имя: {self.name}, идентификационный номер: {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self):
        return "Я работаю с проектами"

    def get_info(self):
        return f"Имя: {self.name}, идентификационный номер: {self.id}, отдел: {self.department}"

class Technican():
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_mainentrance(self):
        return "Я выполняю техническое обслуживание"

    def get_info(self):
        return f"Имя: {self.name}, идентификационный номер: {self.id}, специализация: {self.specialization}"

class TechManager():
    def __init__(self, name, id, specialization, department):
        Technican.__init__(self, name, id, specialization)
        Manager.__init__(self, name, id, department)
        self.emp = []

    def perform_mainentrance(self):
        return Technican.perform_mainentrance(self)

    def add(self, w):
        self.emp.append(w)

TechManager1 = TechManager("Егор", "1234", "Гл. инженер", "Робототехники")

TechManager1.add("Менеджер Вадим")
print(TechManager1.emp)
print(TechManager1.perform_mainentrance())