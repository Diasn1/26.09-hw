class User:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password

    def get_username(self):
        print(self.__username)

    def set_username(self, new_username):
        self.__username = new_username

    def get_email(self):
        print(self.__email)

    def set_email(self, new_email):
        self.__email = new_email

    def get_password(self):
        print(self.__password)

    def set_password(self, new_password):
        self.__password = new_password

    def display_user_info(self):
        print(f"Логин: {self.__username}, Email: {self.__email}")

    def validate_password(self, input_password):
        if input_password == self.__password:
            print("Вы в системе!")
            return True
        else:
            print("Неверный пароль!")
            return False

user1 = User("alice123", "alice@example.com", "securepassword")
user1.display_user_info()
user1.set_username("alice_new")
user1.display_user_info()
user1.get_password()
input_password = input("Введите пароль: ")
user1.validate_password(input_password)