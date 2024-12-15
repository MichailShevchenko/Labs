class UserAccount():
    """Аккаунт пользователя"""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        if self.__check_password(a):
            self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def __check_password(cls, a):
        if a == password:
            print(True)
        else:
            print(False)




    def get_info(self):
        return self.username, self.email, self.__password




UserAccount1 = UserAccount("Kotopyos", "Kotopyosik_nyawka@meowoof.com", "qwerty12345")
print(UserAccount1.get_info())

a = str(input())

UserAccount1.set_password(a)
print(UserAccount1.get_info())


