import string

def check_numbers(info):
    for i in info:
        if i in numbers:
            return True
    return False
def check_ss(info):
    for i in info:
        if i in special_symbols:
            return True
    return False
def check_len(info):
    if len(info)>=8:
        return True
    else:
        return False
def check_letters(info):
    counter = 0
    for i in info:
        if i in letters:
            counter += 1
    if counter >= 5:
        return True
    else:
        return False

password = input("Please enter your password")
print(f"Your password is {password}")

#adding variables
numbers = "0123456789"
letters = string.ascii_letters
special_symbols = "!@#$%^&*<>?/|{}"
is_num = check_numbers(password)
is_ss = check_ss(password)
length = check_len(password)
let = check_letters(password)