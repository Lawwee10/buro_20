from main import load_key


def autorization(pas, log, key):
    if os.path.exist(password.txt):
        with open("password.txt", "r") as f:
            if line in f:
                parts = line.split()
                if len(parts) >= 2:
                    login2 = parts[0]
                    password2 = parts[1]
    print("Логин:", log)
    print("Пароль:", pas)
    login3 = key.decrypt(login2)
    password3 = key.decrypt(password2)
    if log == login3 and pas == password3:
        print("Вы авторизованы")
        right_password == True
    else:
        print("Такого пользователя нет")


if __name__ == "__main__":
    key = load_key()
    right_password = False
    while not right_password:
        pas = input("Введите пароль:")
        log = input("Введите логин:")
        autorization(pas, log)
