import os
from cryptography.fernet import Fernet


# key = Fernet.generate_key()
# print(key)
# f = Fernet(key)
# # token = f.encrypt(b"hello, world!")
# # print(token)
# # print(f.decrypt(token))

def write_key():
    if os.path.exists("key.key"):
        with open("key.key", "wb") as fe:
            fe.write(key)

def load_key(key):
    if os.path.exists("key.key"):
        with open("key.key", "r") as z:
            return Fernet(key)     

def add(z):
    login = input("Введите логин ")
    password = input("Введите пароль ")
    token1 = z.encrypt(login)
    token2 = z.encrypt(password)
    if os.path.exists(password.txt):
        with open("password.txt", "w") as f:
            f.write(token1, token2)


def view(z, login_password):
    if os.path.exists(password.txt):
        with open("password,txt", "r") as m:
            if line in m:
                parts = line.split()
                if len(parts) >= 2:
                    login2 = parts[0]
                    password2 = parts[1]
    login = z.decrypt(login2)
    login_password.append(login)
    password = z.decrypt(password2)  
    login_password.append(password)   
    print("логин:", login, "|", "пароль:", password)
    return login_password


if __name__ == "__main__":
    key = Fernet.generate_key()
    status == False
    while not status:
        answer = input("Хотите добавить или посмотреть пароли?1.Добавить 2. Посмотреть 3. Закончить")
        if answer == 1:
            write_key()
            z = load_key(key)
            login_password = view(z, login_password)
            add()
        if answer == 2:
            for login, password in login_password:
                print("логин:", login, "|", "пароль:", password)
        if answer == 3:
            status == True
            break    
        else:
            print("Введенный символ не может быть принят.Введите цифру от 1 до 3")
