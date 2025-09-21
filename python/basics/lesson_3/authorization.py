from main import load_key

def autorization(pas, log):
    if os.path.exist(password.txt):
        with open("password.txt", "r") as f


if __name__ == "__main__":
    key = load_key()
    right_password = False
    while not right_password:
        pas = input("Введите пароль:")
        log = input("Введите логин:")
        autorization(pas, log)
