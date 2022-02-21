import datetime

from dateutil.relativedelta import relativedelta


def print_hi(to):
    print(f"Hello {to}!")

def ask_a_name():
    name = input("Please, enter your name: ")
    return name

def get_fact(x):
    if x == 1:
        return 1
    else:
        return x * get_fact(x-1)

def get_birth_date():
    while True:
        date = input("Please, enter your birth date in format (DD.MM.YYYY): ")
        try:
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
        except:
            print('Wrong format. Try again!')
        else:
            break
    return date

def user_age(birth_date):
    current_date = datetime.datetime.now()
    time_passed = current_date - birth_date
    print(f"Today is {current_date.strftime('%d.%m.%Y')}, you are {time_passed.days // 365} years ({time_passed.days} days) old")

def main():
    print_hi('World')
    name = ask_a_name()
    print_hi(name)
    name_length = len(name)
    print(f"Your name has {name_length} letters. {name_length}! = {get_fact(name_length)}")
    birth_date = get_birth_date()
    user_age(birth_date)


if __name__ == '__main__':
    main()
