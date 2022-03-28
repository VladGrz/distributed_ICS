import subprocess

def splitter(text):
    text = text.split()
    command = text.pop(0)
    params = text
    return command, params


def ping(params):
    stroka = ''.join(params)
    result = subprocess.getoutput(f"ping {stroka}")
    print(result)


def echo(params):
    print(" ".join(params))


def login(params):
    if len(params) != 2:
        print("Вхід не виконано. Має бути два параметри: <login> <password>")
    else:
        print("Успішно виконав вхід.")


def list(params):
    stroka = ''.join(params)
    result = subprocess.getoutput(f"dir {stroka}")
    print(result)


def msg(params):
    if len(params) != 2:
        print("Лист не надіслано! Має бути два параметри: <destinationUser> <text>")
    else:
        print(f"Лист надіслано користувачу {params[0]}.")


def file(params):
    if len(params) != 2:
        print(
            "Файл не надіслано! Має бути два параметри: <destinationUser> <filename>")
    else:
        print(f"Файл '{params[1]}' надіслано користувачу {params[0]}.")


def main():
    command, params = splitter(input("Введіть команду\n"))
    print(f"Команда: {command}; Параметри: {params}")
    if command == 'ping':
        ping(params)
    elif command == 'echo':
        echo(params)
    elif command == 'login':
        login(params)
    elif command == 'list':
        list(params)
    elif command == 'msg':
        msg(params)
    elif command == 'file':
        file(params)
    elif command == 'exit':
        return False
    else:
        print("Не розпізнав команду спробуйте ще раз")
    return True

if __name__ == "__main__":
    while True:
        if main() == False:
            break
